from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio import config 



def main():
    """MP3   الــكـــريــم  القــــرأن   """
    put_image('https://gate.ahram.org.eg/Media/News/2020/12/10/19_2020-637431900287851167-785.jpg',width='900px',height='200px')
    put_html('<center> <h3> موقع للقـــــرأن الكــريـــم </h3></center>').style('background-color:#D2B48C;padding:2px;')
    put_html('<p>🍃 هاذا الموقع تابع لقناة التلجرام صِدَقِةِ جَاެࢪيَةِ </p> ').style('text-align:center; font-weight:bold;')
    put_html("""  
             
        <ul>
             <li> mp3 القران الـــكريم </li>
        </ul>

        <details id='y'>
             <summary>🎙 المصـــحف كامل بصوت الشــيخ احمــد العجمي</summary>
             <p>سورة الفـــاتحة </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/001.mp3" type"audio/mp3">
             </audio>
             <p>سورة البـــقرة </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/002.mp3" type"audio/mp3">
             </audio>
             <p>سورة ال عمـران</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/003.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــنســاء </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/004.mp3" type"audio/mp3">
             </audio>

             <p>سورة المــائـدة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/005.mp3" type"audio/mp3">
             </audio>
             <p>سورة الأنــعــام</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/006.mp3" type"audio/mp3">
             </audio>
             <p>سورة الأعـــراف</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/007.mp3" type"audio/mp3">
             </audio>
             <p>سورة الانـفــال</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/008.mp3" type"audio/mp3">
             </audio>
             <p>سورة التــوبـة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/009.mp3" type"audio/mp3">
             </audio>
             <p>سورة يـــونــس</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/010.mp3" type"audio/mp3">
             </audio>
            <p>سورة هـــــــود</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/011.mp3" type"audio/mp3">
             </audio>
             <p>سورة يــوســـف</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/012.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــرعــد</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/013.mp3" type"audio/mp3">
             </audio>
             <p>سورة ابـراهيـم</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/014.mp3" type"audio/mp3">
             </audio>
             <p>سورة الحـــجـر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/015.mp3" type"audio/mp3">
             </audio>
             <p>سورة النــحــل</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/016.mp3" type"audio/mp3">
             </audio>
             <p>سورة الاســــراء</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/017.mp3" type"audio/mp3">
             </audio>
             <p>سورة الكـــهــف</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/018.mp3" type"audio/mp3">
             </audio>
             <p>سورة مــريــــم</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/019.mp3" type"audio/mp3">
             </audio>
             <p>سورة طـــــــــه</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/020.mp3" type"audio/mp3">
             </audio>
             <p>سورة الأنــبــياء</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/021.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــحــــج </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/022.mp3" type"audio/mp3">
             </audio>
             <p>سورة المــؤمـنون</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/023.mp3" type"audio/mp3">
             </audio>
             <p>سورة النــــــور</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/024.mp3" type"audio/mp3">
             </audio>
             <p>سورة الفــرقــان</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/025.mp3" type"audio/mp3">
             </audio>
             <p>سورة الشــعــراء</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/026.mp3" type"audio/mp3">
             </audio>
             <p>سورة النـــمـــل</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/027.mp3" type"audio/mp3">
             </audio>
             <p>سورة القـــصـــص</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/028.mp3" type"audio/mp3">
             </audio>
             <p>سورة العنــكبـوت</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/029.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــــــروم</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/030.mp3" type"audio/mp3">
             </audio>
             <p>سورة لقـــمـــان</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/031.mp3" type"audio/mp3">
             </audio>
             <p>سورة الســجــدة </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/032.mp3" type"audio/mp3">
             </audio>
             <p>سورة الأحــــزاب</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/033.mp3" type"audio/mp3">
             </audio>
             <p>سورة ســــــبـأ</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/034.mp3" type"audio/mp3">
             </audio>
            <p>سورةفـــــاطـــر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/035.mp3" type"audio/mp3">
             </audio>
             <p>سورة يــــــــس</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/036.mp3" type"audio/mp3">
             </audio>
             <p>سورة الصــافـات</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/037.mp3" type"audio/mp3">
             </audio>
             <p>سورة ص</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/038.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـزمـــر </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/039.mp3" type"audio/mp3">
             </audio>
             <p>سورة غــافــــر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/040.mp3" type"audio/mp3">
             </audio>
            
             <p>سورة فــــصلــت</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/041.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــــشورى</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/042.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـزخـــرف</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/043.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـدخـــان</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/044.mp3" type"audio/mp3">
             </audio>
             <p>سورة الجــاثـية</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/045.mp3" type"audio/mp3">
             </audio>
             <p>سورة الأحــقــاف</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/046.mp3" type"audio/mp3">
             </audio>
             <p>سورة مـــحـمــد</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/047.mp3" type"audio/mp3">
             </audio>
             <p>سورة الفــتـــح</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/048.mp3" type"audio/mp3">
             </audio>
             <p>سورة الحــجـرات</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/049.mp3" type"audio/mp3">
             </audio>
             <p>سورة ق</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/050.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـذريــات</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/051.mp3" type"audio/mp3">
             </audio>
             <p>سورة الطـــــور</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/052.mp3" type"audio/mp3">
             </audio>
             <p>سورة النــجــم </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/053.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـقــمـر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/054.mp3" type"audio/mp3">
             </audio>
             <p>سورة الرحــمان</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/055.mp3" type"audio/mp3">
             </audio>
             <p>سورة الواقــعة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/056.mp3" type"audio/mp3">
             </audio>
             <p>سورة الحـديــد</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/057.mp3" type"audio/mp3">
             </audio>
             <p>سورة المجادلـة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/058.mp3" type"audio/mp3">
             </audio>
             <p>سورة الحـــشـر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/059.mp3" type"audio/mp3">
             </audio>
             <p>سورة المـمتحنة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/060.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــصـــف</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/061.mp3" type"audio/mp3">
             </audio>
             <p>سورة الجــمـعة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/062.mp3" type"audio/mp3">
             </audio>
             <p>سورة المنافقون </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/063.mp3" type"audio/mp3">
             </audio>
             <p>سورة التــغابـن</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/064.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـطــــلاق</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/065.mp3" type"audio/mp3">
             </audio>
             <p>سورة التـحريــم </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/066.mp3" type"audio/mp3">
             </audio>
             <p>سورة المـــلــك </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/067.mp3" type"audio/mp3">
             </audio>
             <p>سورة القـــلـــم</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/068.mp3" type"audio/mp3">
             </audio>
             <p>سورة الحـــاقـــة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/069.mp3" type"audio/mp3">
             </audio>
             <p>سورة المــعـــارج</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/070.mp3" type"audio/mp3">
             </audio>
             <p>سورة نــــــــوح</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/071.mp3" type"audio/mp3">
             </audio>
             <p>سورة الجــــــن</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/072.mp3" type"audio/mp3">
             </audio>
             <p>سورة المــزمــل</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/073.mp3" type"audio/mp3">
             </audio>
             <p>سورة المـــدثـر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/074.mp3" type"audio/mp3">
             </audio>
             <p>سورة القـــيـامة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/075.mp3" type"audio/mp3">
             </audio>
             <p>سورة الانــســـان</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/076.mp3" type"audio/mp3">
             </audio>
             <p>سورة المــرســلات</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/077.mp3" type"audio/mp3">
             </audio>
             <p>سورة النـــبـــأ</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/078.mp3" type"audio/mp3">
             </audio>
             <p>سورة النــازعـات</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/079.mp3" type"audio/mp3">
             </audio>
             <p>سورة عـــبـــــس</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/080.mp3" type"audio/mp3">
             </audio>
             <p>سورة التـــكويـر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/081.mp3" type"audio/mp3">
             </audio>
             <p>سورة الانفــــطار</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/082.mp3" type"audio/mp3">
             </audio>
             <p>سورة المطــفـفين</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/083.mp3" type"audio/mp3">
             </audio>
             <p>سورة الانشـــقـاق</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/084.mp3" type"audio/mp3">
             </audio>
             <p>سورة البــــروج</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/085.mp3" type"audio/mp3">
             </audio>
             <p>سورة الطـــارق</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/086.mp3" type"audio/mp3">
             </audio>
             <p>سورة الأعـــلـــى</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/087.mp3" type"audio/mp3">
             </audio>
             <p>سورة الغــاشـية </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/088.mp3" type"audio/mp3">
             </audio>
             <p>سورة الفـــجـــر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/089.mp3" type"audio/mp3">
             </audio>
             <p>سورة البـــــلـد</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/090.mp3" type"audio/mp3">
             </audio>
             <p>سورة الشــــمــس</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/091.mp3" type"audio/mp3">
             </audio>
             <p>سورة اللـــيـــل</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/092.mp3" type"audio/mp3">
             </audio>
             <p>سورة الضــــحــى</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/093.mp3" type"audio/mp3">
             </audio>
             <p>سورة الشــــــرح</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/094.mp3" type"audio/mp3">
             </audio>
             <p>سورة التــــــين</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/095.mp3" type"audio/mp3">
             </audio>
             <p>سورة العـــلـــق</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/096.mp3" type"audio/mp3">
             </audio>
             <p>سورة القــــــدر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/097.mp3" type"audio/mp3">
             </audio>
             <p>سورة البـــيـنـة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/098.mp3" type"audio/mp3">
             </audio>
             <p>سورة الزلــزلــة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/099.mp3" type"audio/mp3">
             </audio>
             <p>سورة العــاديــات</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/100.mp3" type"audio/mp3">
             </audio>
             <p>سورة القـــرعــة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/101.mp3" type"audio/mp3">
             </audio>
             <p>سورة التــكاثــر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/102.mp3" type"audio/mp3">
             </audio>
             <p>سورة العــــصــر </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/103.mp3" type"audio/mp3">
             </audio>
             <p>سورة الهــــــمزة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/104.mp3" type"audio/mp3">
             </audio>
             <p>سورة الفيـــــــل</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/105.mp3" type"audio/mp3">
             </audio>
             <p>سورة قــــريــــش</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/106.mp3" type"audio/mp3">
             </audio>
             <p>سورة المـــاعــون</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/107.mp3" type"audio/mp3">
             </audio>
             <p>سورة الكـــوثــــر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/108.mp3" type"audio/mp3">
             </audio>
             <p>سورة الكــافـــرون</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/109.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــــنــصــر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/110.mp3" type"audio/mp3">
             </audio>
             <p>سورة المــــســــد</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/111.mp3" type"audio/mp3">
             </audio>
             <p>سورة الاخــــــــلاص</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/112.mp3" type"audio/mp3">
             </audio>
             <p>سورة الفـــــلـــق</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/113.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـــنـــــاس</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/ajm/128/114.mp3" type"audio/mp3">
             </audio>
             
        </details>
        
             

        <details id='y'>
             <summary>🎙 المصـــحف كامل بصوت الشيخ ياسر الدوسري </summary>
             <p>سورة الفـــاتحة </p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/001.mp3" type"audio/mp3">
             </audio>
             <p>سورة البـــقرة </p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/002.mp3" type"audio/mp3">
             </audio>
             <p>سورة ال عمـران</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/003.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــنســاء </p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/004.mp3" type"audio/mp3">
             </audio>

             <p>سورة المــائـدة</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/005.mp3" type"audio/mp3">
             </audio>
             <p>سورة الأنــعــام</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/006.mp3" type"audio/mp3">
             </audio>
             <p>سورة الأعـــراف</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/007.mp3" type"audio/mp3">
             </audio>
             <p>سورة الانـفــال</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/008.mp3" type"audio/mp3">
             </audio>
             <p>سورة التــوبـة</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/009.mp3" type"audio/mp3">
             </audio>
             <p>سورة يـــونــس</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/010.mp3" type"audio/mp3">
             </audio>
            <p>سورة هـــــــود</p>
             <audio controls>mp3
                 <source src="https://server11.mp3quran.net/yasser/011.mp3" type"audio/mp3">
             </audio>
             <p>سورة يــوســـف</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/012.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــرعــد</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/013.mp3" type"audio/mp3">
             </audio>
             <p>سورة ابـراهيـم</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/014.mp3" type"audio/mp3">
             </audio>
             <p>سورة الحـــجـر</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/015.mp3" type"audio/mp3">
             </audio>
             <p>سورة النــحــل</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/016.mp3" type"audio/mp3">
             </audio>
             <p>سورة الاســــراء</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/017.mp3" type"audio/mp3">
             </audio>
             <p>سورة الكـــهــف</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/018.mp3" type"audio/mp3">
             </audio>
             <p>سورة مــريــــم</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/019.mp3" type"audio/mp3">
             </audio>
             <p>سورة طـــــــــه</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/020.mp3" type"audio/mp3">
             </audio>
             <p>سورة الأنــبــياء</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/021.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــحــــج </p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/022.mp3" type"audio/mp3">
             </audio>
             <p>سورة المــؤمـنون</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/023.mp3" type"audio/mp3">
             </audio>
             <p>سورة النــــــور</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/024.mp3" type"audio/mp3">
             </audio>
             <p>سورة الفــرقــان</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/025.mp3" type"audio/mp3">
             </audio>
             <p>سورة الشــعــراء</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/026.mp3" type"audio/mp3">
             </audio>
             <p>سورة النـــمـــل</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/027.mp3" type"audio/mp3">
             </audio>
             <p>سورة القـــصـــص</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/028.mp3" type"audio/mp3">
             </audio>
             <p>سورة العنــكبـوت</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/029.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــــــروم</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/030.mp3" type"audio/mp3">
             </audio>
             <p>سورة لقـــمـــان</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/031.mp3" type"audio/mp3">
             </audio>
             <p>سورة الســجــدة </p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/032.mp3" type"audio/mp3">
             </audio>
             <p>سورة الأحــــزاب</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/033.mp3" type"audio/mp3">
             </audio>
             <p>سورة ســــــبـأ</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/034.mp3" type"audio/mp3">
             </audio>
            <p>سورةفـــــاطـــر</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/035.mp3" type"audio/mp3">
             </audio>
             <p>سورة يــــــــس</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/036.mp3" type"audio/mp3">
             </audio>
             <p>سورة الصــافـات</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/037.mp3" type"audio/mp3">
             </audio>
             <p>سورة ص</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/038.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـزمـــر </p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/039.mp3" type"audio/mp3">
             </audio>
             <p>سورة غــافــــر</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/040.mp3" type"audio/mp3">
             </audio>
            
             <p>سورة فــــصلــت</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/041.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــــشورى</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/042.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـزخـــرف</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/043.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـدخـــان</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/044.mp3" type"audio/mp3">
             </audio>
             <p>سورة الجــاثـية</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/045.mp3" type"audio/mp3">
             </audio>
             <p>سورة الأحــقــاف</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/046.mp3" type"audio/mp3">
             </audio>
             <p>سورة مـــحـمــد</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/047.mp3" type"audio/mp3">
             </audio>
             <p>سورة الفــتـــح</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/048.mp3" type"audio/mp3">
             </audio>
             <p>سورة الحــجـرات</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/049.mp3" type"audio/mp3">
             </audio>
             <p>سورة ق</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/050.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـذريــات</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/051.mp3" type"audio/mp3">
             </audio>
             <p>سورة الطـــــور</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/052.mp3" type"audio/mp3">
             </audio>
             <p>سورة النــجــم </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/053.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـقــمـر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/054.mp3" type"audio/mp3">
             </audio>
             <p>سورة الرحــمان</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/055.mp3" type"audio/mp3">
             </audio>
             <p>سورة الواقــعة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/056.mp3" type"audio/mp3">
             </audio>
             <p>سورة الحـديــد</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/057.mp3" type"audio/mp3">
             </audio>
             <p>سورة المجادلـة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/058.mp3" type"audio/mp3">
             </audio>
             <p>سورة الحـــشـر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/059.mp3" type"audio/mp3">
             </audio>
             <p>سورة المـمتحنة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/060.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــصـــف</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/061.mp3" type"audio/mp3">
             </audio>
             <p>سورة الجــمـعة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/062.mp3" type"audio/mp3">
             </audio>
             <p>سورة المنافقون </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/063.mp3" type"audio/mp3">
             </audio>
             <p>سورة التــغابـن</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/064.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـطــــلاق</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/065.mp3" type"audio/mp3">
             </audio>
             <p>سورة التـحريــم </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/066.mp3" type"audio/mp3">
             </audio>
             <p>سورة المـــلــك </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/067.mp3" type"audio/mp3">
             </audio>
             <p>سورة القـــلـــم</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/068.mp3" type"audio/mp3">
             </audio>
             <p>سورة الحـــاقـــة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/069.mp3" type"audio/mp3">
             </audio>
             <p>سورة المــعـــارج</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/070.mp3" type"audio/mp3">
             </audio>
             <p>سورة نــــــــوح</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/071.mp3" type"audio/mp3">
             </audio>
             <p>سورة الجــــــن</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/072.mp3" type"audio/mp3">
             </audio>
             <p>سورة المــزمــل</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/073.mp3" type"audio/mp3">
             </audio>
             <p>سورة المـــدثـر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/074.mp3" type"audio/mp3">
             </audio>
             <p>سورة القـــيـامة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/075.mp3" type"audio/mp3">
             </audio>
             <p>سورة الانــســـان</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/076.mp3" type"audio/mp3">
             </audio>
             <p>سورة المــرســلات</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/077.mp3" type"audio/mp3">
             </audio>
             <p>سورة النـــبـــأ</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/078.mp3" type"audio/mp3">
             </audio>
             <p>سورة النــازعـات</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/079.mp3" type"audio/mp3">
             </audio>
             <p>سورة عـــبـــــس</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/080.mp3" type"audio/mp3">
             </audio>
             <p>سورة التـــكويـر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/081.mp3" type"audio/mp3">
             </audio>
             <p>سورة الانفــــطار</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/082.mp3" type"audio/mp3">
             </audio>
             <p>سورة المطــفـفين</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/083.mp3" type"audio/mp3">
             </audio>
             <p>سورة الانشـــقـاق</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/084.mp3" type"audio/mp3">
             </audio>
             <p>سورة البــــروج</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/085.mp3" type"audio/mp3">
             </audio>
             <p>سورة الطـــارق</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/086.mp3" type"audio/mp3">
             </audio>
             <p>سورة الأعـــلـــى</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/087.mp3" type"audio/mp3">
             </audio>
             <p>سورة الغــاشـية </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/088.mp3" type"audio/mp3">
             </audio>
             <p>سورة الفـــجـــر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/089.mp3" type"audio/mp3">
             </audio>
             <p>سورة البـــــلـد</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/090.mp3" type"audio/mp3">
             </audio>
             <p>سورة الشــــمــس</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/091.mp3" type"audio/mp3">
             </audio>
             <p>سورة اللـــيـــل</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/092.mp3" type"audio/mp3">
             </audio>
             <p>سورة الضــــحــى</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/093.mp3" type"audio/mp3">
             </audio>
             <p>سورة الشــــــرح</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/094.mp3" type"audio/mp3">
             </audio>
             <p>سورة التــــــين</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/095.mp3" type"audio/mp3">
             </audio>
             <p>سورة العـــلـــق</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/096.mp3" type"audio/mp3">
             </audio>
             <p>سورة القــــــدر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/097.mp3" type"audio/mp3">
             </audio>
             <p>سورة البـــيـنـة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/098.mp3" type"audio/mp3">
             </audio>
             <p>سورة الزلــزلــة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/099.mp3" type"audio/mp3">
             </audio>
             <p>سورة العــاديــات</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/100.mp3" type"audio/mp3">
             </audio>
             <p>سورة القـــرعــة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/101.mp3" type"audio/mp3">
             </audio>
             <p>سورة التــكاثــر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/102.mp3" type"audio/mp3">
             </audio>
             <p>سورة العــــصــر </p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/103.mp3" type"audio/mp3">
             </audio>
             <p>سورة الهــــــمزة</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/104.mp3" type"audio/mp3">
             </audio>
             <p>سورة الفيـــــــل</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/105.mp3" type"audio/mp3">
             </audio>
             <p>سورة قــــريــــش</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/106.mp3" type"audio/mp3">
             </audio>
             <p>سورة المـــاعــون</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/107.mp3" type"audio/mp3">
             </audio>
             <p>سورة الكـــوثــــر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/108.mp3" type"audio/mp3">
             </audio>
             <p>سورة الكــافـــرون</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/109.mp3" type"audio/mp3">
             </audio>
             <p>سورة الــــنــصــر</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/110.mp3" type"audio/mp3">
             </audio>
             <p>سورة المــــســــد</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/111.mp3" type"audio/mp3">
             </audio>
             <p>سورة الاخــــــــلاص</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/112.mp3" type"audio/mp3">
             </audio>
             <p>سورة الفـــــلـــق</p>
             <audio controls>
                 <source src="https://server10.mp3quran.net/yasser/113.mp3" type"audio/mp3">
             </audio>
             <p>سورة الـــنـــــاس</p>
             <audio controls>
                 <source src="https://server11.mp3quran.net/yasser/114.mp3" type"audio/mp3">
             </audio>
             
        </details>
        
        <a href="https://t.me/sadaka_g" style="background-color: #49A3CC; color: white; padding: 10px 15px; text-decoration: none; border-radius: 10px; display: inline-block;">Telegrame</a>
    
        <a href="https://x.com/Titou__x" style="background-color: #000004; color: white; padding: 10px 48px; text-decoration: none; border-radius: 10px; display: inline-block;">X</a>

        <a href="https://t.me/RakwanCodeRK" style="background-color: #D2B48C; color: white; padding: 10px 15px; text-decoration: none; border-radius: 10px; display: inline-block;">GroupCode</a>
        
        
        
        <hr>
        <p>هاذا الموقع بحقوق @ مشرف قناة صدقة جارية </p>
    """).style('directoin:rtl; text-align:right;')
    put_link("Telegrame", "https://t.me/sadaka_g")



   
if __name__ == '__main__':

    start_server(main , port=34346 ,debug=True)

