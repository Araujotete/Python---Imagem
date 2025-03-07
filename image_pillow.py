from PIL import Image # type: ignore

# mostrar
imagem = Image.open("c:\Users\Robson Araújo\Desktop\Ester Araújo\Imagens\java imagem.jpg")

imagem.show()

# converter (save as jpg)
# tentar direto, se der erro, tornar RGB e converter em jpg
imagem_rgb = imagem.convert("RGB")
imagem_rgb.save("c:\Users\Robson Araújo\Desktop\Ester Araújo\Imagens\java imagem.jpg")

# resize (muito util em servidores/sites) - sempre partindo da maior para a menor, se n você zoa o rolê
tamanho = (500, 500)
imagem.thumbnail(tamanho)
imagem.save("c:\Users\Robson Araújo\Desktop\Ester Araújo\Imagens\java imagem.jpg")

tamanho = (300, 300)
imagem.thumbnail(tamanho)
imagem.save("c:\Users\Robson Araújo\Desktop\Ester Araújo\Imagens\java imagem.jpg")

# editar a imagem

# rotate
imagem.rotate(180).save("c:\Users\Robson Araújo\Desktop\Ester Araújo\Imagens\java imagem.jpg")

# preto e branco
imagem.convert("L").save("c:\Users\Robson Araújo\Desktop\Ester Araújo\Imagens\java imagem.jpg")

# filtros
from PIL import ImageFilter # type: ignore

imagem.filter(ImageFilter.GaussianBlur(20)).save("c:\Users\Robson Araújo\Desktop\Ester Araújo\Imagens\java imagem.jpg")