import numpy as np
from scipy.linalg import svd
from pywt import dwt2

def compress(image, k=50):
    # Aplicar DWT
    coeffs = dwt2(image, 'haar')
    # Aplicar SVD na matriz de coeficientes
    U, S, V = svd(coeffs[0])
    # Selecionar os k primeiros valores singulares para manter
    U_k = U[:, :k]
    S_k = S[:k]
    V_k = V[:k, :]
    # Reconstruir a imagem comprimida
    reconstructed_coeffs = np.dot(U_k, np.dot(np.diag(S_k), V_k))
    # Retornar a imagem comprimida
    return reconstructed_coeffs
