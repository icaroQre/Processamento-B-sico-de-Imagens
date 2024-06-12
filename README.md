## Funções Implementadas

### 1. Separação de Canais RGB

A função `split_channels` separa os três canais de cor (Vermelho, Verde e Azul) de uma imagem e os exibe individualmente.

```python
def split_channels(img_path):
    img = cv2.imread(img_path)
    b, g, r = cv2.split(img)
    cv2.imshow('Blue Channel', b)
    cv2.imshow('Green Channel', g)
    cv2.imshow('Red Channel', r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

### 2. Conversão de RGB para Tons de Cinza
A função rgb_to_grayscale converte uma imagem colorida (RGB) em uma imagem em tons de cinza.

```python
def rgb_to_grayscale(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
### 3. Conversão de Tons de Cinza para Preto e Branco (Limiarização Manual)
A função grayscale_to_black_white aplica um limiar manual a uma imagem em tons de cinza para convertê-la em uma imagem binarizada (preto e branco).

```python
def grayscale_to_black_white(img_path, threshold):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    _, binarized = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binarized Image', binarized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
### 4. Filtro da Média
A função mean_filter aplica um filtro da média a uma imagem, suavizando-a.

```python
def mean_filter(img_path, ksize):
    img = cv2.imread(img_path)
    filtered = cv2.blur(img, (ksize, ksize))
    cv2.imshow('Mean Filter', filtered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
### 5. Filtro da Mediana
A função median_filter aplica um filtro da mediana a uma imagem, removendo ruídos de maneira mais eficaz do que o filtro da média.

```python
def median_filter(img_path, ksize):
    img = cv2.imread(img_path)
    filtered = cv2.medianBlur(img, ksize)
    cv2.imshow('Median Filter', filtered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
### 6. Rotação de Imagem em 90 Graus
```

A função rotate_image gira a imagem em 90 graus no sentido horário.

```python
def rotate_image(img_path):
    img = cv2.imread(img_path)
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('Rotated Image 90 Degrees', rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

### 7. Inversão de Imagem (Horizontal/Vertical)
A função flip_image inverte a imagem horizontalmente ou verticalmente, conforme especificado.

```python
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
```
    
### Exemplo de Uso
```python
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
```
### Como Executar
Certifique-se de ter a biblioteca OpenCV instalada:
```
pip install opencv-python
```

Salve o código acima em um arquivo chamado processamento_imagem.py.
Substitua 'your_image.jpg' pelo caminho da sua imagem.
Execute o script:
```
python processamento_imagem.py
```

Ao executar o script, as janelas do OpenCV abrirão para mostrar os resultados de cada operação de processamento de imagem. Pressione qualquer tecla para fechar as janelas.
