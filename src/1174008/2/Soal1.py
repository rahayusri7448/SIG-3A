import shapefile #mengimport shapefile
w=shapefile.Writer('Soal1') #membuat file bernama Soal1
w.shapeType #mendeklarasikan(memanggil) shape type = default
w.field("kolom1","C") #membuat field pertama 
w.field("kolom2","C") #membuat field kedua
w.record("ngek","satu") #membuat record pertama
w.record("ngok","dua") #membuat record kedua
w.point(1,1) #membuat point pertama denan titik x dan y
w.point(2,2) #membuat point kedua denan titik x dan y
w.close() #menghentikan perintah