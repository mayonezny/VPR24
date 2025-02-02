init:
    # Определение персонажей игры.
    define b = Character('Борис', color="#3c00ff", callback=name_callback, cb_name="b")
    define g = Character('Гоша', color="#ccff00e0", callback=name_callback, cb_name="g")
    define p = Character('Поркшеян', color="#ff0000", callback=name_callback, cb_name="p")
    define n = Character('Никита', color="#eeff00", callback=name_callback, cb_name="n")
    define z = Character('Женя', color="#FFFF00", callback=name_callback, cb_name="z")
    define a = Character('Арина', color="#ff008c", callback=name_callback, cb_name="a")
    define a_s = Character('?Арина?', color="#FF0000", callback=name_callback, cb_name="a_a")
    define s_s = Character('Серега', color="#26ff00", callback=name_callback, cb_name="s_s")
    define d = Character('Ваня', color="#8000ff", callback=name_callback, cb_name="d")
    define s = Character('Стас', color="#F4A460", callback=name_callback, cb_name=None)
    define i = Character('Иван Васильевич', сolor="#1b2780", callback=name_callback, cb_name="i")
    define v = Character('Все', color="#ffffff", callback=name_callback, cb_name=None)
    define author = Character('Автор', color="#FFFFFF", callback=name_callback, cb_name=None)
    define stud = Character('Студенты', сolor="#00eaff", callback=name_callback, cb_name=None)

    # Для :
    define nvl_1 = Character(None, kind=nvl)

    # Теги для анимированного текста
    # дефолт: b - жирный, i - курсив, \n - конец строки, u - подчеркивание, color=#FFFFFF - задать цвет, cps - скорость вывода текста
    # bt - текст волной (bt = 20 амплитуда высоты букв)
    # fi - плавное появление текста (fi = 1-10-100, 1 параметр хз чо делает, 2 параметр время появления, 3 параметр расстояние)
    # sc - дрожащий текст (sc = 20 задать дрожание)
    # rotat - вращение текста (rotat = 20 скорость вращение текста задает) 
    # explode - взрыв текста (explode = 5 задать время через которое произойдет взрыв(в секундах))
    # explodehalf - сильный взрыв текста (explode = 0-2 центр и время разрыва)
    # glitch - глючный текст (glitch = 50% процент глюка)
    # gradient - цвет1-цвет2 (градиент текст)
    # Курсор
    define config.mouse = {"default" : [("gui/cursor.png", 0, 0)]}

    # Нестандартные позиции персонажей
    define left2 = Position(xalign=0.25)
    define right2 = Position(xalign=0.75)

    # Задники:
    image DGTU_BG_INSIDE = "bg/DGTU_BG_INSIDE.jpg"
    image DGTU_BG_OUTSIDE = "bg/DGTU_BG_OUTSIDE.jpg"
    image PARA_L = "bg/PARA_L.jpg"
    image APELSIN = "bg/APELSIN.jpg"
    image PARADISE = "bg/RAI.jpg"
    image SEREGA_ZVONOK = "bg/SEREGA_ZVONOK.jpg"
    image KORIDOR = "bg/KORIDOR.jpg"
    image HELL = "bg/HELL.jpg"
    image PROLOG_OCEAN = "bg/PROLOG_OCEAN.jpg"
    image NA_ULIZE = "bg/NA_ULIZE.jpg"
    image BLACK_SCREEN = "bg/BLACK_SCREEN.jpg"
    image KABINET_DEKANA = "bg/KABINET_DEKANA.jpg"
    image 1_319 = "bg/1_319.jpg"
    image ODINOCHKA = "bg/ODINOCHKA.jpg"
    image PARA_2 = "bg/PARA_2.jpg"
    image PARA_2 = "bg/PARA_2.jpg"
    image PARA_KOMP = "bg/PARA_KOMP.jpg"
    image OBSHAGA = "bg/OBSHAGA.jpg"
    image OBSHAGA_KUHNYA = "bg/OBSHAGA_KUHNYA.jpg"
    image OBSHAGA_VHOD = "bg/OBSHAGA_VHOD.jpg"

    # Спрайты боряна:
    image BORYA_OUTSIDE = At("sprites/BORYA/BORYA_OUTSIDE.png", sprite_highlight("b"))
    # Спрайты Гоги:
    image GOGA_OUTSIDE = At("sprites/GOGA/GOGA_OUTSIDE.png", sprite_highlight("g"))
    # Спрайты Поркша:
    image VPORKSHEYAN = At("sprites/PORKSH/VPORKSHEYAN.png", sprite_highlight("p"))
    # Спрайты Никиты:
    image NIKITA_OUTSIDE = At("sprites/NEKIT/NIKITA_OUTSIDE.png", sprite_highlight("n"))
    # Спрайты Арины:
    image ARINA_OUTSIDE = At("sprites/ARINA/ARINA_OUTSIDE.png", sprite_highlight("a"))
    image ARINA_SUCCUB = At("sprites/ARINA/ARINA_SUCCUB.png", sprite_highlight("a_a"))
    # Спрайты Жени:
    image ZHENYA_OUTSIDE = At("sprites/ZHENYA/ZHENYA_OUTSIDE.png", sprite_highlight("z"))
    # Спрайты Сереги:
    image SEREGA = At("sprites/SEREGA/SEREGA.png", sprite_highlight("s_s"))
    # Спрайты Вани:
    image DIVAN_SERIOUS = At("sprites/DIVAN/DIVAN_SERIOUS.png", sprite_highlight("d"))
    image DIVAN_CRY = At("sprites/DIVAN/DIVAN_CRY.png", sprite_highlight("d"))
    image DIVAN_SMILE = At("sprites/DIVAN/DIVAN_SMILE.png", sprite_highlight("d"))

    # Спрайты Ивана Васильевича:
    image IVAN_VASILIICH = At("sprites/IVAN_VASILIICH/IVAN_VASILIICH.png", sprite_highlight("i"))

    default HP = 5
    default uspevaemost = 0
    default karma = 10
    default sociofob = 0
    
    python:

        renpy.music.register_channel("bgs", "sfx", loop = True)
    
# Игра начинается здесь(пролог):
label start:
    scene PROLOG_OCEAN
    play music "music/neheart_-_snowfall_75941790.mp3"
    author "{glitch}{sc}Что есть жизнь?{/sc}{/glitch}"
    author "Жизнь - это дар, что бы познавать себя и знать, как сотворить прекрасное для своей души, которая способна жить, перемещаясь в любые измерения..."
    author "{glitch=10}{sc=10}...ГДЕ ЕСТЬ ЖИЗНЬ{/sc}{/glitch}"
    author "А душа - это что?"
    author "Это вы и есть внутри себя. человек думает и чувствует внутри себя таким, какой он есть, но выразить это словами не может..."
    author "...боится что его не поймут другие. "
    author "А что такое судьба? И существует ли она?"
    author "Есть мнение, что человек не может изменить свою судьбу? Это правда!"
    author "Судьба не поддается влиянию и изменению. Вопрос в том предначертана ли судьба?"
    author "Ведь если бы это было так, то по факту мы с вами становимся марионетками в чей-то большой игре под названием судьба."
    author "Это как определенный сценарий, в котором нам как читателям все известно."
    author "Но..."
    stop music fadeout (2.0)
    play bgs "sounds/alarm-clock-beep-1_zjgin-vd.mp3"
    author "..."
    author "..."
    author "..."
    author "...Что?"
    show OBSHAGA
    with dissolve
    stop bgs
    play music "music/Мышь - Жвачка.mp3" fadein(2.0)
    window hide
    pause
    window show
    "Ой-ой-ой моя голова..."
    "8 УТРА ?"
    window hide
    pause
    window show
    "Понедельник..."
    "Так..."
    with hpunch
    "ТВОЮ МАТЬ!{w} У меня же сегодня учеба!"
    "Щас еще опоздаю и буду отчислен еще даже не придя ни на одну пару..."
    "БЕГОМ"
    "Стас взял пропуск и вышел из общаги"
    hide OBSHAGA
    show NA_ULIZE
    with dissolve
    stop music
    play bgs "sounds/zvuki-na-ulice-goroda.mp3"
    s "Быстрей, быстрей, идем на взлет!"
    s "Так 1 корпус..."
    s "..."
    s "Ага! Аудитория 384"
    s "Ну с Богом"
    stop bgs
    hide NA_ULIZE
    show BLACK_SCREEN
    with dissolve
    s "Так-с...{w} Ну что же...{w} Хех"
    hide BLACK_SCREEN
    show PROLOG_OCEAN
    with dissolve
    play music "music/neheart_Reidenshi_-_distorted_memories_75718831.mp3"
    s "Эм всем привет! Как вы поняли меня зовут Стас{w} и это моя история"
    s "Недавно мне стукнуло 19 лет, так что родители сказали: либо ты учишься либо идешь в армию"
    s "Меня 2 вариант не устроил..."
    s "И по этой причине я сейчас здесь{w} в Донском Государственном Техническом Университете"
    s "Но я бы хотел начать с начала..."
    s "Я решил попробовать свои силы в рамках новой образовательной программы под названием: \"Школа X\""
    s "И вроде по началу мне даже нравилось:{w} я ходил на пары, работал в команде, да и товарищи были рядом..."
    s "Но что-то не то..."
    s "..."
    s "Не клеилась моя учёба на 1 курсе"
    s "В один момент я решился поговорить со своим деканом.."
    stop music
    show KABINET_DEKANA
    play sound "sounds/stuk-v-dver-kostyashkami-paltsev.mp3"
    s "Иван Васильич можно?"
    show IVAN_VASILIICH
    with dissolve
    i "Проходи, присаживайся"
    s "Иван Васильич, у меня к вам есть разговор"
    i "В чем дело?"
    s "Я хочу перевестись..."
    i "Почему? Тебя что-то не устраивает?"
    s "Ну нет, но...{w} В общем да меня не устраивает мое текущее положение"
    i "Есть ли какая-то веская причина твоего решения?"
    s "Иван Васильевич, сейчас у меня сложный период в жизни"
    i "Может быть я могу чем-то помочь? У меня есть знакомый психолог хороший, можешь ему высказаться, тебе полегчает"
    s "Нет, простите со мной все в порядке{w}, меня просто...."
    s "...напрягает что на меня давят родители{w} и сейчас..."
    s "...и сейчас я в сложной жизненной ситуации{w}, пожалуйста войдите в мое положение, прошу вас..."
    i "Эх...{w} Станислав, ты хорошо учишься так что я сделаю исключение для тебя"
    s "Спасибо!"
    i "Я подготовлю документы"
    s "Хорошо, спасибо вам"
    hide IVAN_VASILIICH
    hide KABINET_DEKANA
    show PROLOG_OCEAN
    with dissolve
    play music "music/neheart_Reidenshi_-_distorted_memories_75718831.mp3"
    s "Итак, я оказался в группе ВПР24..."
    s "Не знаю верный ли был это выбор, но..."
    s "...уже выбора точно нет"
    s "Так что вперед и с песней!"
    s "Надеюсь, что со второго раза мне повезет!"
    author "А может и нет)"
    hide PROLOG_OCEAN
    stop music
    show NA_ULIZE
    with dissolve
    play bgs "sounds/zvuki-na-ulice-goroda.mp3"
    s "Черт, надо спешить"
    s "Опаздываю"
    stop bgs
    show DGTU_BG_INSIDE
    with dissolve
    play bgs "sounds/turniket.mp3"
    s "Так пропуск, где же ты"
    s "Ага нашел!"
    s "Давай же долбанный турникет!"
    s "Есть!"
    s "3 этаж..."
    stop bgs
    play sound "sounds/dgtu_zvon.mp3"
    s "Твою мать! Быстрее! На первую же пару опаздывать..."
    show PARA_L
    with fade
    s "Так! Это вроде тут..."
    s "Заходим"
    stop sound
    jump DGTU_OUTSIDE

label DGTU_OUTSIDE:
    play bgs "sounds/zvuki-na-ulice-goroda.mp3"
    scene DGTU_BG_OUTSIDE
    show BLACK_SCREEN
    with dissolve
    "Тем временем..."
    hide BLACK_SCREEN
    with dissolve
    g "Боря быстрей, сейчас опоздаем, нас Поркш убьёт!"
    show GOGA_OUTSIDE at left2
    show BORYA_OUTSIDE at right2
    with dissolve
    b "Да иду я уже"
    g "О Ванек дарова"
    show GOGA_OUTSIDE at left
    show BORYA_OUTSIDE at right
    with move
    show DIVAN_SMILE at center
    with dissolve
    d "Дарова! Че вы тут стоите?"
    g "Как-никак тебя ждем"
    d "А пара скоро?"
    b "Да вот через..."
    d "Да пофиг, я курить. {w}Если что я опоздаю!"
    b "Ага, пофиг!{w} У тебя мало того что долг, так еще и посещаемость решил \"исправить\"?"
    g "Вот именно! Tак что никаких курить." 
    g "Пойдем. У нас теорвер"
    d "Ладно..."
    d "На ковер к Поркшу не особо хочется..."
    hide DIVAN_SMILE
    hide NIKITA_OUTSIDE
    show NIKITA_OUTSIDE at left2
    with dissolve
    n "Всем здарова челики! A че вы не на паре?"
    n "Идем, а то опоздаем"
    show ZHENYA_OUTSIDE at right2
    with dissolve
    z "Я уже устал 60 заказов в день выполнять, сдохну скоро"
    z "Староста пойдем уже"
    hide DIVAN_SMILE
    show ARINA_OUTSIDE at center
    with dissolve
    a "Да задолбали{w}, НЕ НАЗЫВАЙТЕ МЕНЯ СТРОСТОЙ!"
    stop music fadeout(2.0)
    stop bgs fadeout(2.0)
    hide NIKITA_OUTSIDE
    hide BORYA_OUTSIDE
    hide ZHENYA_OUTSIDE
    hide ARINA_OUTSIDE
    show GOGA_OUTSIDE at center
    with dissolve
    g "Я думаю нам пора"
    g "Пойдем!"
    jump in_DGTU

label in_DGTU:
    scene DGTU_BG_INSIDE
    play bgs "sounds/turniket.mp3"
    show BORYA_OUTSIDE
    with dissolve
    b "Ух, мы внутри"
    hide BORYA_OUTSIDE
    show GOGA_OUTSIDE
    with dissolve
    g "Ага, давай быстрей, а то опоздаем на пару"
    stop bgs fadeout(2.0)
    play sound "sounds/dgtu_zvon.mp3"
    hide GOGA_OUTSIDE
    show ZHENYA_OUTSIDE
    with dissolve
    z "Погодите! Я карту найти не могу"
    # Спрайт Арины
    a "Да пошли уже задолбал"
    stop sound fadeout(3.0)
    jump NA_PARE_PORKHA

label NA_PARE_PORKHA:
    scene PARA_L
    show BLACK_SCREEN
    with dissolve
    "В это время в 1-384..."
    hide BLACK_SCREEN
    show VPORKSHEYAN
    with dissolve
    play music "sounds/DELTA_SHTRIX.mp3"
    "~ Блин как скучно... ~"
    "~ Как они его лекции слушают только? ~"
    window hide
    pause
    window show
    "~ О опоздал кто-то ~"
    p "Пара уже 10 минут идет вы где ходите?"
    v "Простите за опоздание, Виталий Маркосович!"
    p "Чтобы это было в последний раз"
    p "{glitch}{sc}{color=#ff0000}{b}Иначе следующего раза не будет{/b}{/color}{/sc}{/glitch}"
    "Слава Богу я не опоздал..."
    p "Так, продолжаем..."
    window hide
    pause
    pause
    pause
    window show
    "~ Не я не могу уже... Cкууука ~"
    window hide
    menu:
        "Уснуть":
            p "Чтобы продемонстрировать вам..."
            stop music fadeout(2.0)
            $ uspevaemost -= 1
            show BLACK_SCREEN 
            with dissolve
            "..."
            "..."
            "..."
            play sound "sounds/dgtu_zvon.mp3"
            hide VPORKSHEYAN
            hide BLACK_SCREEN
            show PARA_L
            with dissolve
            s "Ой что уже все что-ли?"
        "Внимательно слушать":
            $ uspevaemost += 1
            nvl_1 "{b}Теория вероятностей{/b} — это наука, которая изучает мир случайностей и пытается их предсказать. Здесь встречаются такие понятия, как «события» и «вероятности», у которых, в свою очередь, есть свои свойства и операции — о них мы поговорим чуть позже."
            nvl_1 "Проще всего продемонстрировать, как работает теория вероятностей, на примере подбрасывания монетки. В этом случае у нас есть два варианта: орёл или решка, а значит, шанс выпадения каждой из сторон одинаковый и составляет 50\%."
            nvl_1 "Но как убедиться, что это действительно так? Например, я могу подбросить монетку десять раз, и мне магическим образом девять раз подряд выпадет орёл и один раз решка. Значит ли это, что шанс выпадения орла — 90\%? Конечно, нет — и у этого есть научное объяснение."
            nvl_1 "Дело в том, что теория вероятностей рассматривает случайные события в рамках бесконечности. Иными словами, если мы будем подбрасывать монетку бесконечное количество раз, то шансы выпадения орла или решки будут приближаться к 50\%."
            nvl_1 "Такая же логика работает и для других случайных явлений — например, шанс выпадания числа 5 на игральном кубике равен 1 к 6, а вероятность того, что молния ударит в одно и то же место дважды — примерно 1 к 500."
            nvl_1 "Теория вероятностей помогает нам предсказывать шанс возникновения различных событий, когда ответ не такой однозначный и на события влияет множество факторов."
            nvl_1 "Мы упомянули слова «событие» и «вероятность», но не рассказали, что они вообще значат в контексте теории вероятностей. Давайте разбираться."
            nvl_1 "{b}Событие{/b} — это всё, что может произойти, когда мы совершаем какое-то действие. Например, если мы бросаем монетку, то событие — это выпадение орла или решки. Чтобы обозначать события, используют заглавные буквы латинского алфавита. Например, для орла можем выбрать букву A, а для решки — B."
            nvl_1 "Существует много разных видов и классификаций событий, но на этой лекции мы остановимся на основных четёрых:"
            nvl_1 "{b}Достоверные{/b} — те, которые точно произойдут. Если бросить стакан на пол, то с вероятностью 100\% он полетит вниз."
            nvl_1 "{b}Невозможные{/b} — те, которые никогда не произойдут. Если бросить тот же стакан на пол, то он никогда не полетит вверх."
            nvl_1 "Мораль: не стоит бросать стаканы на пол, если, конечно, вы не на МКС"
            stud "Ахахахах"
            nvl_1 "{b}Случайные{/b} — те, которые могут произойти, а могут и не произойти. Например, если мы бросаем игральный кубик, то не можем с уверенностью сказать, что выпадет число 2."
            nvl_1 "{b}Несовместимые{/b} — те, которые исключают друг-друга. Например, при подбрасывании монетки может выпасть либо орёл, либо решка — оба одновременно они выпасть не могут."
            nvl_1 "Если собрать все несовместимые события вместе, они будут называться полной группой событий. Это множество событий, одно из которых обязательно случится, если мы совершаем действие, а другие — не произойдут никогда. Например, когда мы бросаем игральный кубик, может выпасть только одна из сторон."
            nvl_1 "А теперь поговорим про непосредственно вероятность"
            nvl_1 "{b}Вероятность{/b} — это число, которое обозначает шанс возникновения события. Например, вероятность выигрыша в лотерею может составлять 1 к 1 000 000."
            nvl_1 "Мы записывали значения вероятностей в процентах и отношениях, но математикам удобнее располагать их в диапазоне от 0 до 1. Если вероятность равна 0, то событие никогда не произойдёт, а если 1 — точно произойдёт. Всё, что посередине, — это случайные события."
            nvl_1 "Самый простой способ вычислить вероятность — поделить число благоприятных событий на общее число возможных событий."
            nvl_1 "Например, если всего в колоде 36 карт, а мы хотим достать короля пик, то вероятность этого события равна 1/36, или 0,03. Если бы нас устроил любой из королей, то вероятность была бы равна 4/36 — то есть 0,1."
            nvl_1 "К формулам мы ещё вернёмся, а пока отметим, что вероятность — это не всегда точное предсказание, а лишь оценка шанса возникновения события. Как следует из закона больших чисел, если шанс выпадения орла и решки равен 50\%, это не означает, что они будут выпадать по очереди."
            nvl_1 "Ещё вероятность может быть условной — или зависеть от другого события. Например, если мы хотим вытащить любой туз из колоды карт, шанс равен 4/36."
            nvl_1 "Но если до этого кто-то уже вытащил одного туза, то вероятность будет равна 3/35. Это потому, что в колоде стало на одну карту меньше и количество благоприятных событий тоже уменьшилось."
            nvl_1 "С определениями закончили — теперь давайте узнаем, как событиями можно управлять..."
            window hide
            pause   
            stop music fadeout(2.0)        
            play sound "sounds/dgtu_zvon.mp3"
            hide VPORKSHEYAN
            with dissolve
            s "Неужели{w}, я думал усну епта"
    s "Так нужно бы \"своих\" для начала найти. Познакомиться хоть" # альтернатива: s 'Так нужно бы "своих" для начала найти. Познакомиться хоть'
    stop bgs fadeout(1.0)
    jump POSLE_PARI_PORKHA

label POSLE_PARI_PORKHA:
    scene KORIDOR 
    with dissolve
    play music "sounds/Universitet.mp3"
    "~ Выйдя из аудитории я увидел нескольких ребят ~"
    show GOGA_OUTSIDE
    show ZHENYA_OUTSIDE at right
    show BORYA_OUTSIDE at left
    with dissolve
    window hide
    menu:
        "Подойти к ним":
            $ sociofob -= 1
            window show
            g "Капец пара душная"
            z "Согласен лучше бы дома поспал"
            b "Аче я в ДГТУ в куртке ?"
            "Я не нашел другого спрайта...сорян..."
            z "У нас 10 минут еще есть"
            hide GOGA_OUTSIDE
            with dissolve
            show DIVAN_SMILE at center
            with dissolve
            d "О! Получается мы с Женей идем курить?!"
            z "Погнали!"
            hide ZHENYA_OUTSIDE 
            with dissolve
            hide DIVAN_SMILE
            with dissolve
            "Женя с Ваней ушли на апельсин"
            show GOGA_OUTSIDE with dissolve
            g "Идем, иначе опоздаем"
            s "Эй, ребят вы ВПР24?"
            g "Да, а что ты хотел?"
            s "О значит мне по адресу, меня зовут Станислав, можно просто - Стас"
            g "А нам Серега говорил что новенький седня должен был прийти"
            g "Меня, если что, Гоша зовут"
            g "Это Борис"
            b "Дарова я да"
            g "А это Ва..."
            g "О..."
            g "Они уже свалили"
            g "..."
            g "Ууу! Hам в 8 корпус... Идем скорее, иначе опоздаем"

        "Лучше пройду мимо":
            window show
            "~ Думаю что не стоит подходить, а то обознаюсь еще ~"
            $ sociofob += 1

    stop music fadeout(2.0)
    jump SECOND_PARA

label SECOND_PARA:
    if (sociofob > 0): 
        scene ODINOCHKA
        play music "sounds/Universitet.mp3"
        "~ Так-с аудитория 1-3ХХ ~"
        "~ Ага, нашел! Вроде не опоздал ~"
        show GOGA_OUTSIDE at right2
        show BORYA_OUTSIDE at left2
        with dissolve
        "~ Хм, у этих ребят видимо, пара здесь же, может стоило подойти к ним? ~"
        window hide
        pause
        window show        
        "~ Только их вроде было четверо ... ~"
        hide GOGA_OUTSIDE
        hide BORYA_OUTSIDE
        with dissolve
        pause
        "~ В любом случае времени на это уже нет ~"
        "~ Пора в аудиторию ~"
        hide ODINOCHKA
        scene PARA_KOMP
        with fade
        "Стас вошел в аудиторию"
        "В ней он снова увидел этих ребят"
        show GOGA_OUTSIDE at left2
        show BORYA_OUTSIDE at right2
        with dissolve
        g "О! Привет! Ты новенький?"
        "Стас неохотно подходит к ребятам"
        s "Да"
        b "Нам Серый говорил что к нам человечек со Школы Х переводится"
        g "Угу." 
        g "Как тебя зовут?"
        s "Станислав."
        s "Для друзей просто Стас"
        b "Ну тогда будем считать что мы уже дружим"
        b "Я Боря. А это Гоша"
        g "Даров"
        "Пожимают руки"
        "~ А они вроде дружелюбные ~"
        "~ Думаю мы подружимся ~"
    else:
        scene PARA_KOMP
        play music "sounds/Universitet.mp3"
        show GOGA_OUTSIDE at left2
        show BORYA_OUTSIDE at right2
        with dissolve
        g "Ну вроде успели"
        s "А что у нас сейчас?"
        g "Какая-то херня. Карен потом придумает"
        b "Кайф"
        
    show GOGA_OUTSIDE at left
    show BORYA_OUTSIDE at left2
    with move
    show Какой-то_Препод at right
    with dissolve
    "Какой-то Препод" "Так, ребята."
    "Какой-то Препод" "Все на места."
    "Какой-то Препод" "Пара началась"
    return

label DEATH_BAD:
    scene HELL
    play bgs "sounds/HELL_KRIK.mp3"
    author "Пизда тебе"
    "БЛЯТЬ ЧТО ГДЕ Я?"
    "..."
    "..."
    "..."
    "..."
    "..."
    show ARINA_SUCCUB
    a_s "Ну привет"
    " - Концовка: Вечность с Ариной - "
    return

label DEATH_GOOD:
    scene PARADISE
    author "ТЫ ЕБЛАН ВСЕ HP ПРОЕБАЛ"
    return
