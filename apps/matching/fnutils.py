import cv2
import numpy as np
import glob

FINGERPRINT_FOLDER = 'database'
data_images = {}

def get_match(route):
    test_image_rgb = cv2.imread(route)
    test_image_gray = cv2.cvtColor(test_image_rgb, cv2.COLOR_BGR2GRAY)
    test_image_vector = np.matrix(test_image_gray.ravel()).T
    error_values = {}
    aproximations = {}
    folders = glob.glob(f'{FINGERPRINT_FOLDER}/*')
    get_data_images(folders)
    #Calcula la descomposición SVD de cada matriz correspondiente a las huellas de una persona
    sub_matrix_u = get_descomposition()
    min_error = None
    for sub, U in sub_matrix_u.items():
        try:
            alpha = U.T @ test_image_vector
            aproximation = U @ alpha
            residual_vector = test_image_vector - aproximation
            norm_residual = np.linalg.norm(residual_vector)
            error_values[sub] = norm_residual #Almacena los errores
            aproximations[sub] = aproximation
            if not min_error:
                min_error = (sub, norm_residual, aproximation)
            else:
                if norm_residual < min_error[1]:
                    min_error = (sub, norm_residual, aproximation)
        except:
            return 0, None
    if min_error[1] > 1:
        return 0, None
    return 100, min_error[0]

def get_data_images(folders):
    for folder in folders:
        sub_name = folder.split('\\')[1]
        data_images[sub_name] = []
        for image in glob.glob(f'{folder}/*.jpg'):
            sub_image = cv2.imread(image)
            sub_gray_image = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
            data_images[sub_name].append(sub_gray_image)
    return data_images

def get_descomposition(sub_matrix_u={}):
    for sub, images in data_images.items():
        flat_vectors = []
        for image in images:
            flat_image = image.ravel()
            flat_vectors.append(flat_image)
        X = np.matrix(flat_vectors).T
        U, S, VT = np.linalg.svd(X, full_matrices=False)
        sub_matrix_u[sub] = U
    return sub_matrix_u