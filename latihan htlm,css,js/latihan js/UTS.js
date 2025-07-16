
console.log("Masukan Pilihan Anda")
console.log("1. Linux, Standar, RP. 150.000")
console.log("2. Windows, Medium, RP. 300.000")
console.log("3. Mac, VIP, RP. 1.000.000")


var bayar;
var bonus;
var Total;
var pilihan = prompt("masukan pilihan Kamar : ");
var lama = prompt("berapalama ingin menginap : ");
var member = prompt("apakah kamu member [y=1/n=0] : ");

switch(pilihan){
    case 1 :
        bayar = 150000*lama
        break;
    case 2 :
        bayar = 300000*lama
        break;
    case 3 :
        bayar = 1000000*lama
        break;
}

if (member == 1) {
    bonus = bayar*0.10;      
} 

if (lama < 3) {
    hasil = 0.5*(bayar-bonus);
} 
Total = bayar-bonus-hasil; 
console.log("Biaya yang harus anda bayar : "+Total);