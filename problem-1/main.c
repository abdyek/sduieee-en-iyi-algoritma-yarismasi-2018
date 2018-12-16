#include<stdio.h>
#include<stdlib.h>

struct nokta {
    struct nokta * onceki;  // gezgin pointer ı için geçmişi tutmamız gerekiyor,
    struct nokta * k[10];   // gidilebilir komşu dizisi, 10 dan fazlaysa burayı düzenlemeniz gerekiyor
    int id;              // noktayı diğerlerinden ayıran sayı
    int bakilacak;
};

struct nokta * noktaUret(int id) {
    struct nokta * nkt = (struct nokta *)malloc(sizeof(struct nokta));
    nkt->id = id;
    nkt->bakilacak = 0;
    return nkt;
}


int main() {

    // bizden istenen örümcen ağını noktalar ile modelleyelim
    struct nokta * n[22];   // 0. elemanı boş bırakayım, böylece dizi indisi ile nokta id si aynı olsun

    for(int k = 1; k<=22; k++) {
        n[k] = noktaUret(k);
    }

    /* Bizden istenen örümcek ağının F noktasından başlayarak saat yönünde noktaları numaralandırdım.
     * Bu numaralandırmaya göre F noktası 1 id li nokta, S noktası 6 id li nokta oluyor
    */
    struct nokta * baslangic = n[6];    // S noktası
    struct nokta * gezgin = baslangic;  // while içerisinde gezecek gezgin pointerı
    struct nokta * hedef = n[1];        // F noktası

    // ürettiğimiz 21 noktayı birbirine bağlayalım
    n[2]->k[0] = n[1];  // türkçesi , 2 noktası 1 noktasına gidebilir
    n[3]->k[0] = n[2];
    n[4]->k[0] = n[3];
    n[4]->k[1] = n[14];
    n[5]->k[0] = n[4];
    n[5]->k[1] = n[15];
    n[6]->k[0] = n[5];
    n[6]->k[1] = n[16];
    n[6]->k[2] = n[7];
    n[7]->k[0] = n[17];
    n[7]->k[1] = n[8];
    n[8]->k[0] = n[18];
    n[8]->k[1] = n[9];
    n[9]->k[0] = n[10];
    n[10]->k[0] = n[1];
    n[11]->k[0] = n[1];
    n[12]->k[0] = n[11];
    n[12]->k[1] = n[2];
    n[13]->k[0] = n[12];
    n[13]->k[1] = n[3];
    n[14]->k[0] = n[13];
    n[14]->k[1] = n[21];
    n[15]->k[0] = n[14];
    n[15]->k[1] = n[21];
    n[16]->k[0] = n[15];
    n[16]->k[1] = n[21];
    n[16]->k[2] = n[17];
    n[17]->k[0] = n[21];
    n[17]->k[1] = n[18];
    n[18]->k[0] = n[21];
    n[18]->k[1] = n[19];
    n[19]->k[0] = n[20];
    n[19]->k[1] = n[9];
    n[20]->k[0] = n[11];
    n[20]->k[1] = n[10];
    n[21]->k[0] = n[13];
    n[21]->k[1] = n[12];
    n[21]->k[2] = n[11];
    n[21]->k[3] = n[20];
    n[21]->k[4] = n[19];

    // yalancı nokta (algoritmamdaki pürüzlü bir yer için)
    struct nokta * yalanciNokta = noktaUret(30);
    n[6]->k[3] = yalanciNokta;

    // yukarıdaki gibi tek yön gidişli farklı modeller oluşturulup uygulanabilir, bir yalancıNokta oluşturup başlangıca komşu yapmayı unutmayın


    int enKisaYol = 100;     // hedefe ulaşmak için en kısa yol
    int topYolSay = 0;       // hedefe ulaşmak için toplam yol sayısı

    int alinanYol = 0;       // hedefe ulaşmak için alinan yol

    while(baslangic->k[baslangic->bakilacak]!=NULL) {
        if(gezgin->k[gezgin->bakilacak]!=NULL)  {
            //printf("%d ", gezgin->id);       // test amaçlı
            gezgin->bakilacak++;          
            gezgin->k[gezgin->bakilacak-1]->onceki = gezgin; 
            gezgin = gezgin->k[gezgin->bakilacak-1];
            //printf("--> %d\n", gezgin->id); // test amaçlı
            alinanYol++;
            if(hedef->id==gezgin->id) {
                if(alinanYol<enKisaYol){
                    enKisaYol = alinanYol;
                }
                topYolSay++;
            }
        } else {
            gezgin->bakilacak = 0;          // gezginin o andaki bulunduğu noktaya tekrar uğrama ihtimaline karşı sıfırlama işlemi yapılıyor
            //printf("%d ", gezgin->id);  // test amaçlı
            gezgin = gezgin->onceki;
            //printf("--> %d !dönüş! \n", gezgin->id); // test amaçlı
            alinanYol--;
        }
    }
    // ^ test amaçlı satır kodlarının önündeki yorum satırı işaretini kaldırırsanız bütün adımları monitör edebilirsiniz
   
    printf("En kısa yolun uzunluğu : %d birim\n", enKisaYol);
    printf("Hedefe ulaşmak için toplam yol sayısı : %d\n", topYolSay);

    return 0;
}




