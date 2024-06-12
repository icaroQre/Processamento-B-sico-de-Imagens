import cv2

# Função para separar canais RGB
def split_channels(img_path):
    img = cv2.imread(img_path)
    b, g, r = cv2.split(img)
    cv2.imshow('Blue Channel', b)
    cv2.imshow('Green Channel', g)
    cv2.imshow('Red Channel', r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Função para converter RGB para tons de cinza
def rgb_to_grayscale(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Função para converter tons de cinza para preto e branco (limiarização manual)
def grayscale_to_black_white(img_path, threshold):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    _, binarized = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binarized Image', binarized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Função para aplicar filtro da média
def mean_filter(img_path, ksize):
    img = cv2.imread(img_path)
    filtered = cv2.blur(img, (ksize, ksize))
    cv2.imshow('Mean Filter', filtered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Função para aplicar filtro da mediana
def median_filter(img_path, ksize):
    img = cv2.imread(img_path)
    filtered = cv2.medianBlur(img, ksize)
    cv2.imshow('Median Filter', filtered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Função para girar imagem em 90 graus
def rotate_image(img_path):
    img = cv2.imread(img_path)
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('Rotated Image 90 Degrees', rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Função para inverter imagem (horizontal/vertical)
def flip_image(img_path, horizontal=True):
    img = cv2.imread(img_path)
    if horizontal:
        flipped = cv2.flip(img, 1)
        cv2.imshow('Horizontally Flipped Image', flipped)
    else:
        flipped = cv2.flip(img, 0)
        cv2.imshow('Vertically Flipped Image', flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Exemplo de uso
if __name__ == "__main__":
    image_path = 'your_image.jpg'
    
    split_channels(image_path)
    rgb_to_grayscale(image_path)
    grayscale_to_black_white(image_path, 128)
    mean_filter(image_path, 5)
    median_filter(image_path, 5)
    rotate_image(image_path)
    flip_image(image_path, horizontal=True)
    flip_image(image_path, horizontal=False)
