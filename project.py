# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome('C:/Users/정민정/Desktop/chromedriver_win32/chromedriver.exe')

url = 'https://kkutu.cc/'
driver.get(url)

w = driver.find_element_by_class_name("jjo-display ellipse")
def words(w):
    if w == "가":
        return "가까운목장의신선한원유로만든저지방우유"
    elif w == "각":
        return "각성된엘리시아의여왕갑주"
    elif w == "간":
        return "간단한모니터링입니다"
    elif w == "감":
        return "감지금니대방광불화엄경보현행원품"
    elif w == "갑":
        return "갑종배당이자소득세"
    elif w == "갓":
        return "갓잡은새로운생선의세레브니카이도치즈루"
    elif w == "강":
        return "강아지같아서말을걸었더니사실은늑대였습니다"
    elif w == "같":
        return "같은질이가염색체"
    elif w == "개":
        return "개구리는입때문에뱀이꿀꺽한다"
    elif w == "객":
        return "객성이너무도밝은밤"
    elif w == "갤":
        return "갤럭시단조무래기"
    elif w == "갸":
        return "갸오오와사랑꾼들"
    elif w == "거":
        return "거스름이없음을으뜸으로여기라"
    elif w == "건":
        return "건전가정의례의정착및지원에관한법률"
    elif w == "걸":
        return "걸침턱메뚜기장이음"
    elif w == "검":
        return "검정마디꼬리납작맵시벌"
    elif w == "겁":
        return "겁많은둔자스피나"
    elif w == "게":
        return "게이트자위대그의땅에서이처럼싸우며"
    elif w == "겐":
        return "겐잔미요리마사의활"
    elif w == "겔":
        return "겔렌데걸키사라기치하야"
    elif w == "겟":
        return "겟불쥐의옷가나하하비키"
    elif w == "겨":
        return "겨울위도우메이커"
    elif w == "격":
        return "격투기특성화사립고교극지고"
    elif w == "견":
        return "견습신비밀의코코타마"
    elif w == "결":
        return "결혼까지생각했어남친으로부터의탈출"
    elif w == "겸":
        return "겸허한부자를향한편한"
    elif w == "경":
        return "경계의안쪽에숨은영과이상한무녀"
    elif w == "계":
        return "계속되는여름파라다이스마이하마아유무"
    elif w == "고":
        return "고양이를통해만난흔해빠질수있는그와그녀의인연"
    elif w == "골":
        return "골가나르공포의그물거미"
    elif w == "곰":
        return "곰곰히차고르기이부키츠바사"
    elif w == "곱":
        return "곱등어푸른벌레말"
    elif w == "공":
        return "공각기동대어라이즈보더2고스트위스퍼스"
    elif w == "과":
        return "과거의여친님이나에게미소를건네왔다"
    elif w == "관":
        return "관촉사석조미륵보살입상"
    elif w == "광":
        return "광휘기사들의스타라이트페스티벌"
    elif w == "괭":
        return "괭이갈매기울적에"
    elif w == "괴":
        return "괴력의악동브란즈앤드브란셀"
    elif w == "교":
        return "교정뒤에는천사가묻혀있다"
    elif w == "구":
        return "구텐베르크비헤르트불연속면"
    elif w == "국":
        return "국제연합팔레스타인민난구제사업기관"
    elif w == "군":
        return "군위아미타여래삼존석굴"
    elif w == "굳":
        return "굳은알루미니움선"
    elif w == "굴":
        return "굴거리가시꽃파리"
    elif w == "굶":
        return "굶주리는코수모스"
    elif w == "굿":
        return "굿모닝사회인야구"
    elif w == "궁":
        return "궁그닐디센트이그노어가드"
    elif w == "권":
        return "권선징악은옛적의옳은신말씀이니"
    elif w == "궤":
        return "궤변학파요츠야선배의괴담"
    elif w == "귀":
        return "귀자르는네루리님의입학만세만세만만세"
    elif w == "귤":
        return "귤동방랍질깍지벌레"
    elif w == "그":
        return "그녀에게귀와꼬리가달려있는이유를설명할수없다"
    elif w == "극":
        return "극장판마법소녀마도카마기카신편반역의이야기"
    elif w == "근":
        return "근심하는세상은근심의수레"
    elif w == "글":
        return "글러먹은소녀컴페니언요코야마나오"
    elif w == "금":
        return "금색의바람격려의위싱라이브"
    elif w == "급":
        return "급접근스페이스라이드마이하마아유무"
    elif w == "기":
        return "기어오는냐루애니리멤버마이러브크래프트선생"
    elif w == "긴":
        return "긴장의브라이덜게이트키타자와시호"
    elif w == "길":
        return "길잃은마왕의딸이숲속나무꾼부려먹는만화"
    elif w == "김":
        return "김전일소년의1박2일짧은여행"
    elif w == "깃":
        return "깃아가미실바다지렁이"
    elif w == "까":
        return "까칠한임작가의만화그리기"
    elif w == "깔":
        return "깔때기배꼽골뱅이"
    elif w == "깡":
        return "깡통나사고물로봇"
    elif w == "깨":
        return "깨달음의수호자클라한"
    elif w == "꺼":
        return "꺼져라황당한인생"
    elif w == "껍":
        return "껍질보유바이러스"
    elif w == "께":
        return "께람지트콩크리트"
    elif w == "꼬":
        return "꼬마버스타요가좋아하는젤리"
    elif w == "꽃":
        return "꽃피우는인자한자를향한질투"
    elif w == "꾸":
        return "꾸벅꾸벅꿈을꾸는기분시노미야카렌"
    elif w == "꿀":
        return "꿀벌주머니발육체병"
    elif w == "꿈":
        return "꿈꾸는전기양과다재범용의시크릿에이전트"
    elif w == "끌":
        return "끌어당겨엎어뜨리기"
    elif w == "끝":
        return "끝마디통통집게벌레"
    elif w == "끼":
        return "끼있는여자는밤이슬을좋아한다"
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""
    elif w == "":
        return ""

while :
if driver.find_element_by_id()=='당신의 차례! 아래의 채팅 창에서 입력하세요.':
    w = driver.find_element_by_class_name("jjo-display ellipse")
    def words(w)
    driver.find_element_by_name('ChatBtn').click()