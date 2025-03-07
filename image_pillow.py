from PIL import Image # type: ignore

# mostrar
imagem = Image.open("c:\Users\Robson Araújo\Desktop\Ester Araújo\Imagens\java imagem.jpg")

imagem.show()

# converter (save as jpg)
# tentar direto, se der erro, tornar RGB e converter em jpg
imagem_rgb = imagem.convert("RGB")
imagem_rgb.save("imagens/python lira.jpg")

# resize (muito util em servidores/sites) - sempre partindo da maior para a menor, se n você zoa o rolê
tamanho = (500, 500)
imagem.thumbnail(tamanho)
imagem.save("imagens/python lira 500.png")

