from PIL import Image,ImageDraw

def Dissection(minValue, maxValue,path):
    image = Image.open(path)
    draw = ImageDraw.Draw(image)

    height = image.size[0]
    width = image.size[1]

    img =[[int(0)]*width for i in range(height)]


    pix = image.load()

    for i in range(height):
        for j in range(width):
            value = int(0.3 * pix[i,j][0] + 0.59 * pix[i,j][1] + 0.11 * pix[i,j][2])
            if minValue <= value and value <= maxValue:
                draw.point((i,j),(255,255,255))
                img[i][j] = 1
            else:
                draw.point((i,j),(0,0,0))

    for i in range(1,height-1,1):
        for j in range(1,width-1,1):
            if img[i][j] == 0 and img[i-1][j] == 1 and img[i+1][j] == 1 and img[i][j-1] == 1 and img[i][j+1] == 1: 
                img[i][j] = 1
                draw.point((i,j),(0,0,0))

    return image,img