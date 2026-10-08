print("Dame 4 numerines para ver tu nota media")
nota1 = int(input())
nota2 = int(input())
nota3 = int(input())
nota4 = int(input())
nota_media = (nota1+ nota2+ nota3+nota4)/4
if nota_media>90:
    print ("calificacion A")
elif nota_media<89 and nota_media>80:
    print ("calificacion B")
elif nota_media<79 and nota_media>70:
    print("calificacion C")
elif nota_media<69 and nota_media>50:
    print("calificacion D")
elif nota_media<50:
    print("calificacion D")