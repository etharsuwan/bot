from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Replace with your bot token and channel details
TOKEN = '7472868397:AAEDb-PfX44i92d3l_y5Ua0WOPCv-61X-KM'
CHANNELS = ['@sevansevan', '@parkinsonsrabic']

async def check_subscription(user_id, context):
    for channel in CHANNELS:
        try:
            chat_member = await context.bot.get_chat_member(channel, user_id)
            if chat_member.status not in ['member', 'administrator', 'creator']:
                return False
        except Exception:
            return False
    return True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if await check_subscription(user_id, context):
        # Show the main menu
        buttons = [
            [InlineKeyboardButton("الدراسة في روسيا", callback_data='study')],
            [InlineKeyboardButton("العلاج في روسيا", callback_data='medical')],
            [InlineKeyboardButton("السياحة في روسيا", callback_data='tour')],
            [InlineKeyboardButton(" المنحة الدراسية في روسيا", callback_data='gift')],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await update.message.reply_text("اهلاً بك! لطفا اختار من القائمة:", reply_markup=reply_markup)
    else:
        # Prompt to subscribe to channels
        await update.message.reply_text(
            "يرجى الاشتراك بالقنوات التالية لتتمكن من استخدام البوت للاجابة على اسئلتكم بعد متابعتهم يرجى الضغط مرة اخرى على  start/ :\n"
            f"1. {CHANNELS[0]}\n"
            f"2. {CHANNELS[1]}"
        )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'study':
        # Study submenu
        buttons = [
            [InlineKeyboardButton("طريقة التقديم", callback_data='study_option_1')],
            [InlineKeyboardButton("اسعار السكن و المعيشة في روسيا ", callback_data='study_option_2')],
            [InlineKeyboardButton(" تكلفة التقديم والخدمات التي نقدمها", callback_data='study_option_3')],
            [InlineKeyboardButton(" التخصصات والجامعات المتاحة", callback_data='study_multi')],
            [InlineKeyboardButton(" الدول الممنوعة من الدخول الى روسيا", callback_data='study_option_4')],
            [InlineKeyboardButton("أنا جاهز للتقديم",  url=f"https://t.me/sevanrussia")],
            [InlineKeyboardButton("الرجوع للقائمة", callback_data='main_menu')],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text("لطفاً الاختيار من القائمة للاستفسار عن الدراسة في روسيا:", reply_markup=reply_markup)
    

    elif query.data == 'medical':
        # Medical submenu
        buttons = [
            [InlineKeyboardButton("علاج مرض باركنسون وخلل التوتر العضلي", callback_data='parkenson')],
            [InlineKeyboardButton("علاج العيون", url=f"https://t.me/sevanrussia")],
            [InlineKeyboardButton("الرجوع للقائمة", callback_data='main_menu')],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text("يرجى اختيار الخدمة:", reply_markup=reply_markup)

    elif query.data =='parkenson':
        buttons = [
            [InlineKeyboardButton("تعرف على العلاج", callback_data='medical_option_1')],
            [InlineKeyboardButton("الاعراض التي يعالجها", callback_data='medical_option_2')],
            [InlineKeyboardButton("تكلفة العلاج وماذا يشمل", callback_data='medical_option_3')],
            [InlineKeyboardButton("نبذة عن المشفى ", callback_data='medical_option_4')],
            [InlineKeyboardButton("للتواصل مع الاطباء والمختصين", callback_data='medical_option_5')],
            [InlineKeyboardButton("طريقة السفر إلى روسيا لتلقي العلاج", callback_data='medical_option_6')],
            [InlineKeyboardButton(" فيديوهات لحالات تم علاجها بالمشفى", url ="https://www.youtube.com/watch?v=9mgjspUvPa8&list=PLjJ5OPYDRG2c2M1PPHA_EKe2fQQTioDyX")],
            [InlineKeyboardButton(" جاهز للتواصل", url=f"https://t.me/sevanrussia")],

            

            [InlineKeyboardButton("الرجوع للقائمة", callback_data='medical')],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text("تفاصيل العلاج بالموجات فوق الصوتية:", reply_markup=reply_markup)
    elif query.data == 'tour':
        # Study submenu
        buttons = [
            [InlineKeyboardButton("نبذة عن السياحة في روسيا", callback_data='tour_1')],
            [InlineKeyboardButton("اهم المعالم السياحية في روسيا ", callback_data='tour_2')],
            [InlineKeyboardButton("اهم المدن السياحية", callback_data='tour_3')],
            [InlineKeyboardButton(" اسعار السياحة في روسيا", callback_data='tour_4')],
            [InlineKeyboardButton(" افضل اوقات الزيارة", callback_data='tour_5')],
            [InlineKeyboardButton(" التسوق في روسيا", callback_data='tour_6')],
            [InlineKeyboardButton(" التأشيرة", callback_data='tour_7')],
            [InlineKeyboardButton(" فيديوهات لمعالم سياحية", url=f"https://youtube.com/playlist?list=PLjJ5OPYDRG2esSeMPgOF6Pz721V4etEnH&si=IU6XL_-OYT0Uy8LH")],
            [InlineKeyboardButton("للتقديم",  url=f"https://t.me/sevanrussia")],
            [InlineKeyboardButton("الرجوع للقائمة", callback_data='main_menu')],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text("لطفاً الاختيار من القائمة للاستفسار عن السياحة في روسيا:", reply_markup=reply_markup)

                #المنحة الدراسية 
    elif query.data =='gift':
        buttons =[
            [InlineKeyboardButton("التخصصات والجامعة المانحة", callback_data='gift_1')],
            [InlineKeyboardButton("الوثائق المطلوبة ", callback_data='gift_2')],
            [InlineKeyboardButton("معلومات عن المنحة", callback_data='gift_3')],
            [InlineKeyboardButton("الدول المسموح لها التقديم", callback_data='gift_4')],
            [InlineKeyboardButton("للتقديم",  url=f"https://t.me/sevanrussia")],
            [InlineKeyboardButton("الرجوع للقائمة", callback_data='main_menu')],
        ]
        reply_markup= InlineKeyboardMarkup(buttons)
        await query.edit_message_text("لطفاً الاختيار من القائمة للاستفسار عن المنح الدراسية", reply_markup=reply_markup)

    elif query.data =='study_multi':
        buttons =[
            [InlineKeyboardButton("التخصصات الطبية", callback_data='medical_un')],
            [InlineKeyboardButton("التخصصات الهندسية ", callback_data='engineer_un')],
            [InlineKeyboardButton("السنة التحضيرية", callback_data='fresher')],
            [InlineKeyboardButton("الرجوع للقائمة", callback_data='study')],
        ]
        reply_markup= InlineKeyboardMarkup(buttons)
        await query.edit_message_text("لطفاً الاختيار من القائمة للاستفسار عن التخصصات الدراسية", reply_markup=reply_markup)

    elif query.data =='medical_un':
        buttons =[
            [InlineKeyboardButton("جامعة بشكريا الطبية", callback_data='un_1')],
            [InlineKeyboardButton("جامعة موسكو الطبية الاولى", callback_data='un_2')],
            [InlineKeyboardButton("الرجوع للقائمة", callback_data='study_multi')],
        ]
        reply_markup= InlineKeyboardMarkup(buttons)
        await query.edit_message_text("لطفاً الاختيار من القائمة للاستفسار عن الجامعات ", reply_markup=reply_markup)

    elif query.data =='engineer_un':
        buttons =[
            [InlineKeyboardButton("جامعة اوفا للبترول", callback_data='un_3')],
            [InlineKeyboardButton(" جامعة اوفا للعلوم والتكنولوجيا ", callback_data='un_4')],
            [InlineKeyboardButton("الرجوع للقائمة", callback_data='study_multi')],
        ]
        reply_markup= InlineKeyboardMarkup(buttons)
        await query.edit_message_text("لطفاً الاختيار من القائمة للاستفسار عن الجامعات ", reply_markup=reply_markup)

    elif query.data =='fresher':
        buttons =[
            [InlineKeyboardButton("جامعة الاورال الفدرالية", callback_data='un_5')],
            [InlineKeyboardButton("جامعة اوفا للبترول", callback_data='un_6')],
            [InlineKeyboardButton("جامعة اوفا للعلوم والتكنولوجيا", callback_data='un_7')],
            [InlineKeyboardButton("جامعة بشكيريا الحكومية", callback_data='un_8')],


            [InlineKeyboardButton("الرجوع للقائمة", callback_data='study_multi')],
        ]
        reply_markup= InlineKeyboardMarkup(buttons)
        await query.edit_message_text("لطفاً الاختيار من القائمة للاستفسار عن الجامعات ", reply_markup=reply_markup)

    elif query.data == 'main_menu':
        # Main menu
        buttons = [
            [InlineKeyboardButton("الدراسة في روسيا", callback_data='study')],
            [InlineKeyboardButton("العلاج في روسيا", callback_data='medical')],
            [InlineKeyboardButton("السياحة في روسيا", callback_data='tour')],
            [InlineKeyboardButton(" المنحة الدراسية في روسيا", callback_data='gift')],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text("اهلاً بك! لطفا اختار من القائمة:", reply_markup=reply_markup)


    elif query.data == 'un_1':
     response_text = (
        "جامعة بشكيريا الطبية \n\n"
        "*الموقع*:\n"
        " تقع جامعة بشكيريا الطبية في مدينة أوفا، عاصمة جمهورية باشكورتوستان في روسيا. تأسست الجامعة في عام 1932 وتعد واحدة من المؤسسات التعليمية الرائدة في مجال الطب في روسيا. \n\n"
     "*التخصصات*: \n"
     "تقدم الجامعة مجموعة متنوعة من التخصصات الطبية، بما في ذلك: - الطب العام \n- طب الأسنان \n - الصيدلة \n- التمريض\n - التخصصات الطبية الأخرى مثل الطب الوقائي والطب النفسي\n\n"
     "أسعار التخصصات الطبية:\n"
     "تتراوح أسعار الدراسة في جامعة بشكيريا الطبية حسب التخصص واللغة التي تدرس بها (الروسية أو الإنجليزية). إليك نظرة عامة تقريبية على التكاليف:\n"
     "- *الطب العام*: \n"
     " - باللغة الروسية: 3400 دولار سنويًا.\n"
     "  - باللغة الإنجليزية: 5,000  دولار سنويًا.\n\n"

     "- *طب الأسنان*: \n"
     "- باللغة الروسية: حوالي 3400  دولار سنويًا.\n"
     "  - باللغة الإنجليزية: حوالي 5000 دولار سنويًا.\n\n"

     "- *الصيدلة*: \n"
     "- باللغة الروسية: حوالي 3,000  دولار سنويًا.\n\n"

     "- *التمريض*: \n"
     " - باللغة الروسية: حوالي 2,500  دولار سنويًا\n"

    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='medical_un')]]))

    elif query.data == 'un_2':
     response_text = (
        " جامعة موسكو الطبية الأولى (MSMU)\n\n"
"*الموقع*:\n"
" تقع جامعة موسكو الطبية الأولى في العاصمة الروسية موسكو، وهي واحدة من أقدم وأهم الجامعات الطبية في روسيا، تأسست في عام 1758.\n\n"
     "*التخصصات*: \n"
"تقدم الجامعة مجموعة واسعة من التخصصات الطبية، بما في ذلك:\n - الطب العام\n- طب الأسنان\n- الصيدلة\n- التمريض\n- الطب النفسي\n- العلوم الصحية\n\n"

     "أسعار التخصصات الطبية:\n"
"تتراوح أسعار الدراسة في جامعة موسكو الطبية الأولى حسب التخصص واللغة التي تدرس بها (الروسية أو الإنجليزية). إليك نظرة عامة تقريبية على التكاليف:"

     "- *الطب العام*: \n"
     " - باللغة الروسية: 11,000 دولار سنويًا.\n"
     "  - باللغة الإنجليزية: 11,000 دولار سنويًا.\n\n"

     "- *طب الأسنان*: \n"
     "- باللغة الروسية: حوالي 9,000  دولار سنويًا.\n"
     "  - باللغة الإنجليزية: حوالي 11,000 دولار سنويًا.\n\n"

     "- *الصيدلة*: \n"
     "- باللغة الروسية: حوالي 7,000  دولار سنويًا.\n"
     " - باللغة الإنجليزية: 8,000 - دولار سنويًا.\n\n"

     "- *التمريض*: \n"
     " - باللغة الروسية: حوالي 7,000  دولار سنويًا\n\n"
     "**ملاحظات إضافية** \n\n"
     "- *التكاليف الإضافية*: يجب أخذ بعين الاعتبار تكاليف المعيشة في موسكو، والتي قد تتراوح بين 500-1,000 دولار شهريًا حسب نمط الحياة.- ** \n"
     "تعتبر جامعة موسكو الطبية الأولى خيارًا متميزًا للطلاب الذين يسعون للحصول على تعليم طبي عالي الجودة، حيث تتمتع بسمعة قوية على المستوى الدولي وتوفر فرصًا واسعة للبحث والتدريب العملي.\n"

    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='medical_un')]]))

    elif query.data == 'un_3':
     response_text = (
        " جامعة اوفا للبترول  \n\n"
        "*الموقع*:\n"
"تقع جامعة أوفا الحكومية التقنية للبترول في مدينة أوفا، عاصمة جمهورية باشكورتوستان في روسيا. تأسست في عام 1948، وتُعد واحدة من الجامعات التقنية الرائدة في روسيا، حيث تركز على تدريب المتخصصين في مجالات النفط والغاز. \n"  
     "أسعار التخصصات الطبية:\n"
     "تتراوح أسعار الدراسة في جامعة اوفا للبترول حسب التخصص واللغة التي تدرس بها (الروسية أو الإنجليزية). إليك نظرة عامة تقريبية على التكاليف:\n"
     "- *الهندسة الكيميائية*: \n"
     " - باللغة الانجليزية: 2540 دولار سنويًا.\n"
     

     "- *هندسة البترول*: \n"
     "  - باللغة الإنجليزية: حوالي 2600 دولار سنويًا.\n\n"

     "- *الهندسة الكيميائية والميكاترونيكس*: \n"
     "- باللغة الانجليزية: حوالي 2540  دولار سنويًا.\n\n"

     "- *الهندسة الكهربائية والأتمتة*: \n"
     " - باللغة الانجليزية: حوالي 2540 دولار سنويًا\n"

    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='engineer_un')]]))


    elif query.data == 'un_4':
     response_text = (
        "جامعة اوفا للعلوم والتكنولوجيا \n\n"
        "*الموقع*:\n"
"تقع جامعة أوفا للعلوم والتكنولوجيا في مدينة أوفا، عاصمة جمهورية باشكورتوستان، روسيا. تعتبر الجامعة مركزًا أكاديميًا بارزًا، وتشتهر بتقديم برامج تعليمية عالية الجودة في مجالات الهندسة والتكنولوجيا والعلوم.\n\n"  
     "أسعار التخصصات الهندسية:\n"
     "تتراوح أسعار الدراسة في جامعة اوفا للعلوم والتكنولوجيا  حسب التخصص واللغة التي تدرس بها (الروسية أو الإنجليزية). إليك نظرة عامة تقريبية على التكاليف:\n"
     "- *هندسة الكمبيوتر*: \n"
     " - باللغة الروسية: 1725 دولار سنويًا.\n"
     "  - باللغة الإنجليزية: 2529  دولار سنويًا.\n\n"

     "- *الهندسة بجميع فروعها*: \n"
     "- باللغة الروسية: حوالي 1729  دولار سنويًا.\n"

     "- *ميكاترونيكس*: \n"
     "- باللغة انجليزية: حوالي 2853  دولار سنويًا.\n\n"

     "- *امن سبراني*: \n"
     " - باللغة الروسية: حوالي 1729  دولار سنويًا\n\n"

     "- *هندسة طائرات*: \n"
     " - باللغة الانجليزية: حوالي 3529  دولار سنويًا\n\n"

     "- *الفيزياء و الكييمياء و الاحياء*: \n"
     " - باللغة الروسية: حوالي 1717  دولار سنويًا\n\n"

     "- *الرياضيات*: \n"
     " - باللغة الروسية: حوالي 1494  دولار سنويًا\n\n"

     "- *بزنس*: \n"
     " - باللغة الروسية: حوالي 1445  دولار سنويًا\n\n"

     "- *الاقتصاد*: \n"
    " - باللغة الروسية: حوالي 1445  دولار سنويًا\n\n"

     "- *العلاقات الدولية*: \n"
     " - باللغة الانجليزية: حوالي 1623  دولار سنويًا\n\n"
    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='engineer_un')]]))

    elif query.data == 'un_5':
     response_text = (
       " السنة التحضيرية هي سنة اجبارية لكل الطلاب الأجانب الذين لا يجيدون الروسية كلغة للدراسة واختاروا دراسة التخصص باللغة الروسية، يتم فيها تدريس اللغة الروسية بكثافة بالإضافة إلى المصطلحات والمفاهيم الأساسية للتخصص الذي سوف تدرسه بعد التحضيرية، أما عن مكان دراسة التحضيرية فلا يشترط أن تدرسه بنفس الجامعة التي ستدرس بها التخصص\n\n"
"سعر السنة التحضيرية  في جامعة الاورال الفيدرالية: \n"
"1700 دولاراً"
    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='fresher')]]))

    elif query.data == 'un_6':
     response_text = (
       " السنة التحضيرية هي سنة اجبارية لكل الطلاب الأجانب الذين لا يجيدون الروسية كلغة للدراسة واختاروا دراسة التخصص باللغة الروسية، يتم فيها تدريس اللغة الروسية بكثافة بالإضافة إلى المصطلحات والمفاهيم الأساسية للتخصص الذي سوف تدرسه بعد التحضيرية، أما عن مكان دراسة التحضيرية فلا يشترط أن تدرسه بنفس الجامعة التي ستدرس بها التخصص\n\n"
"سعر السنة التحضيرية  في جامعة اوفا للبترول: \n"
"1350 دولاراً"
    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='fresher')]]))
   
    elif query.data == 'un_7':
     response_text = (
       " السنة التحضيرية هي سنة اجبارية لكل الطلاب الأجانب الذين لا يجيدون الروسية كلغة للدراسة واختاروا دراسة التخصص باللغة الروسية، يتم فيها تدريس اللغة الروسية بكثافة بالإضافة إلى المصطلحات والمفاهيم الأساسية للتخصص الذي سوف تدرسه بعد التحضيرية، أما عن مكان دراسة التحضيرية فلا يشترط أن تدرسه بنفس الجامعة التي ستدرس بها التخصص\n\n"
"سعر السنة التحضيرية  في جامعة اوفا للعلوم والتكنولوجيا: \n"
"1300 دولاراً"
    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='fresher')]]))

    elif query.data == 'un_8':
     response_text = (
       " السنة التحضيرية هي سنة اجبارية لكل الطلاب الأجانب الذين لا يجيدون الروسية كلغة للدراسة واختاروا دراسة التخصص باللغة الروسية، يتم فيها تدريس اللغة الروسية بكثافة بالإضافة إلى المصطلحات والمفاهيم الأساسية للتخصص الذي سوف تدرسه بعد التحضيرية، أما عن مكان دراسة التحضيرية فلا يشترط أن تدرسه بنفس الجامعة التي ستدرس بها التخصص\n\n"
"سعر السنة التحضيرية  في جامعة بشكيريا الحكومية: \n"
"2800 دولاراً"
    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='fresher')]]))


    elif query.data == 'gift_1':
     response_text = (
        "جامعة اوفا للبترول\n\n"
     "ماجستير :\n\n MSC Master of Science in oil and gas well drilling \n \n"
     "بكالوريوس: \n\n"
     "هندسة طاقة\n"
     "هندسة بترول\n"
     "هندسة حفريات \n"
     "هندسة جيولوجيا \n"
     "سياحة \n"
     "اقتصاد \n"
     "التصميم \n"
     "الهندسة المعمارية \n"
     "هندسة بترول باللغة الانجليزية\n "

     
    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='gift')]]))

    elif query.data == 'gift_2':
     response_text = (
      "1) جواز السفر (الأصلي)\n"
      "2) وثيقة التعليم (الأصلية)\n"
      "3) شهادة طبية (تتضمن خلو الجسم من التهاب الكبد B و C والسل)\n"
      "4) جواز السفر (الترجمة)\n"
      "5) وثيقة تعليمية (ترجمة)\n"
      "6) شهادة عدم الإصابة بفيروس نقص المناعة البشرية \n"
      "7) خطاب توصية من الجامعة "
     
    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='gift')]]))

    elif query.data == 'gift_3':
     response_text = (
        "مدة الدراسة: \n\n"
     "الماجستير: \n"
    
     "- سنتان للتخصصات باللغة الانجليزية\n"
     "- 3 سنوات للدراسة باللغة الروسية (سنة لغة روسية )\n\n"

     "البكلوريوس:\n"
     
     "- 4 سنوات للتخصصات باللغة الانجليزية\n"
     "- 5 سنوات للدراسة باللغة الروسية (سنة لغة روسية )\n\n"

"الراتب: 30 دولار شهرياً\n\n"
" السكن الجامعي: 300 دولار شهرياً(التكلفة على الطالب)\n\n"
"التذكرة: على الطالب"


    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='gift')]]))

    elif query.data == 'gift_4':
     response_text = (
      "المغرب\n"
      "تونس\n"
      "لبنان\n"
      "السعودية\n"
      "الكويت\n"
      "الإمارات\n"
      "عمان\n"
      "البحرين\n"
     
    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='gift')]]))

    elif query.data == 'study_option_1':
        # Handle طريقة التقديم
        buttons = [
            [InlineKeyboardButton(" اضغط للتواصل", url="https://t.me/sevanrussia")],
            [InlineKeyboardButton("الرجوع للقائمة", callback_data='study')],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text(
            "### خطوات التقديم في روسيا عبر مكتبنا\n\n"
        
            "1. *جمع الوثائق المطلوبة*:\n"
            "   - قم بإعداد الأوراق اللازمة، والتي تشمل:\n"
            "     - صورة من جواز السفر الصالح لمدة تزيد عن 18 شهراً.\n"
            "     - الشهادات الثانوية مصدقة من وزارة الخارجية.\n\n"
            "2. *تقديم الطلب*:\n"
            "   - بعد جمع الوثائق، أرسلها إلينا. سنقوم بملء استمارات الطلب اللازمة وترجمة جميع الوثائق المطلوبة بدقة.\n\n"
            "3. *دفع الرسوم*:\n"
            "   - سنقوم بتزويدك بتفاصيل الرسوم المطلوبة مقابل خدماتنا. بعد إتمام الدفع، سنبدأ في معالجة طلبك.\n\n"
            "4. *متابعة الطلب*:\n"
            "   - سنقوم بمتابعة حالة طلبك بانتظام وتزويدك بالتحديثات. لا تتردد في التواصل معنا في أي وقت للاستفسارات.\n\n"
            "5. *استلام قبولك الجامعي*:\n"
            "   - بعد مراجعة طلبك، سنقوم بإرسال القبول الجامعي لك.\n\n"
            "6. *دفع الرسوم الجامعية*:\n"
            "   - بعد استلام القبول، ستتلقى مستندات رسمية من الجامعة تشمل عقداً يوضح طريقة دفع الرسوم الجامعية والمبلغ المطلوب.\n\n"
            "7. *استخراج الدعوة الدراسية*:\n"
            "   - بعد دفع الرسوم الجامعية، سيتولى مكتبنا دفع الرسوم المطلوبة لاستخراج الدعوة الدراسية وتقديم الأوراق اللازمة عبر الجامعة.\n\n"
            "8. *التخطيط للسفر*:\n"
            "   - بمجرد حصولك على الدعوة الدراسية، يمكنك التوجه إلى السفارة الروسية في بلدك لتقديم طلب الحصول على الفيزا.\n\n"
            "9. *التسجيل عند الوصول*:\n"
            "    - بعد وصولك إلى روسيا، سنساعدك في إتمام جميع الإجراءات المتعلقة بالجامعة، بما في ذلك السكن، تأشيرة الإقامة، استخراج شريحة هاتف، وفتح حساب بنكي.\n\n"
            "---\n\n"
            "إذا كان لديك أي استفسارات إضافية أو تحتاج إلى مزيد من المعلومات، لا تتردد في الاتصال بنا. نحن هنا لدعمك في كل خطوة!",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )


    elif query.data == 'study_option_2':
        # Handle طريقة التقديم
        buttons = [
            [InlineKeyboardButton("الرجوع للقائمة", callback_data='study')],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text(
            " 1. *المدن الكبرى (مثل موسكو)*\n\n"
            "- *الإيجار*: \n"
            "  - سكن جامعي: يتراوح بين 200-400 دولار شهريًا. \n"
            " - شقة خاصة: تتراوح بين 600-1,200 دولار شهريًا، حسب الموقع وحجم الشقة. \n\n"
            "- *الطعام*: \n"
            "  - تكلفة الوجبات في المطاعم: تتراوح بين 5-15 دولار للوجبة الواحدة. \n"
            "  - تكلفة البقالة الشهرية: حوالي 200-300 دولار. \n\n"
            "- *المواصلات*: \n\n"
            "  - تذكرة المواصلات العامة: حوالي 0.5-1 دولار. \n"
            "  - اشتراك شهري للمواصلات: حوالي 20 دولار. \n\n"
            "- *الأنشطة الترفيهية*: \n\n"
            " - تذكرة دخول السينما: حوالي 5-10 دولارات. \n"
            " - تكاليف الأنشطة الأخرى: عادةً ما تكون أقل مقارنة بالمدن الكبرى. \n\n"
            "ملخص \n\n"
            "بشكل عام، تعتبر تكاليف المعيشة في روسيا متنوعة وتعتمد بشكل كبير على المدينة التي تقيم فيها. "
            " المدن الكبرى مثل موسكو أكثر تكلفة، بينما المدن الصغيرة مثل أوفا تقدم خيارات أكثر اقتصادية. من المهم للطلاب التخطيط لميزانيتهم بناءً على هذه التكاليف لتلبية احتياجاتهم اليومية." ,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
   

    elif query.data == 'study_option_3':
        #تكلفة التقديم والخدمات
        services_text = (
          
            "- استخراج القبول الجامعي.\n"
            "- استخراج الدعوة الدراسية من الجامعة.\n"
            "- الاستقبال في المطار.\n"
            "- النقل من المطار إلى الجامعة.\n"
            "- تأمين السكن.\n"
            "- المساعدة في التأمين الصحي.\n"
            "- الترجمة المعتمدة للوثائق.\n"
            "- مساعدة الطلاب في إنهاء إجراءات التأجيل الدراسي للتجنيد والحصول على تصريح السفر.\n"
            "- المساعدة في الفحص الطبي عند الوصول.\n"
            "- المساعدة في التسجيل في الجامعة وفي القسم الخاص بالفيزا.\n"
            "- المساعدة في دفع الرسوم الدراسية الجامعية.\n"
            "- فتح حساب مصرفي في روسيا.\n"
            "- تقديم الدعم لطلابنا خلال فترة دراستهم الكاملة.\n"
            "- ترتيب سكن منفصل خاص للطالبات.\n"
            "- تمديد التأشيرة الدراسية خلال الفترة الدراسية الكاملة.\n"
            "- الدعم والمساعدة للطالب في أي وقت، وتقديم كافة النصائح والإرشادات.\n\n"
            "*كل هذه الخدمات نقدمها بتكلفة 789$*"
        )
        await query.edit_message_text(services_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='study')]]))
    
    elif query.data == 'study_option_4':
      treatment_text = (
        "سوريا\nاليمن \nالعراق \nمصر \nليبيا\n"
    )
      await query.edit_message_text(treatment_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='study')]]))


    elif query.data == 'medical_option_1':
      treatment_text = (
        "*علاج مرض باركنسون باستخدام الموجات فوق الصوتية*\n\n"
        "هو تقنية جديدة نسبيًا تهدف إلى إنهاء الأعراض الحركية للمرض. يعتمد هذا العلاج على استخدام الموجات الصوتية عالية التردد لاستهداف مناطق محددة في الدماغ، مثل النواة المذنبة أو النواة تحت المهاد، التي تلعب دورًا في التحكم في الحركات اللاإرادية.\n\n"
        "*كيفية عمل العلاج:*\n"
        "1. *تحديد الهدف*: يتم تحديد المنطقة المستهدفة في الدماغ باستخدام تقنيات التصوير مثل الرنين المغناطيسي.\n"
        "2. *إرسال الموجات فوق الصوتية*: يتم توجيه الموجات فوق الصوتية إلى المنطقة المحددة. هذه الموجات تتسبب في تسخين الأنسجة وتعديل نشاط الخلايا العصبية.\n"
        "3. *تخفيف الأعراض*: الهدف هو إنهاء الأعراض مثل الرعشة، تصلب العضلات، وصعوبة الحركة.\n\n"
        "*الفوائد:*\n"
        "- *غير جراحي*: العلاج لا يتطلب جراحة، مما يقلل من المخاطر المرتبطة بالعمليات الجراحية التقليدية.\n"
        "- *تحسين جودة الحياة*: يساعد المرضى على استعادة الوظائف الحركية وتحسين جودة حياتهم."
    )
      await query.edit_message_text(treatment_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='parkenson')]]))

   
  

    elif query.data == 'medical_option_2':
      response_text = (
       
            "علاج مرض باركنسون باستخدام الموجات فوق الصوتية يمكن أن يعالج أيضًا:\n\n"
        "*الرعشة:* يعمل العلاج على تقليل أو القضاء على الرعشة الناتجة عن المرض.\n"
        "*التصلب:* يساعد في تخفيف التصلب العضلي المرتبط بمرض باركنسون.\n"
        "*البطء في الحركة:* يعزز القدرة على الحركة بشكل أسرع وأكثر مرونة.\n\n"
        "يستهدف هذا العلاج الأطراف والرأس لتحسين جودة الحياة وتقليل الأعراض الحركية."
       )
      await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='parkenson')]]))
 
    elif query.data == 'medical_option_3':
      response_text = (
        "تكلفة العلاج باستخدام الموجات فوق الصوتية لمرض باركنسون هي 16800$.\n\n"
        "التكلفة تشمل:\n"
        "- العملية\n"
        "- السكن\n"
        "- الطعام\n"
        "- التنقلات من وإلى المطار\n"
        "- التنقلات من وإلى المستشفى\n\n"
        "تستغرق فترة العلاج 5 أيام."
       )
      await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='parkenson')]]))
    elif query.data == 'medical_option_5':
      response_text = (
        "من الضروري أن نتأكد أن العلاج بالموجات فوق الصوتية هو الخيار الأمثل لك. لذا، الخطوة الأولى التي يجب أن نتخذها هي:\n"
        "- إرسال فيديو عن حالتك (دون تأثير الأدوية) إلى طبيب جراحة المخ والأعصاب، بالإضافة إلى التقارير الطبية الخاصة بك.\n\n"
        "قد يطلب الدكتور إجراء مقابلة عبر الإنترنت بتكلفة 5500₽، وذلك للتأكد من حالتك ومدى ملاءمتها للعلاج.\n"
        "يتم دفع المبلغ عبر الموقع الرسمي للمشفى."
        "جميع الملفات يتم ارسالها لنا من خلال الضغط على خيار ارسال الملفات ادناه."
     )
      await query.edit_message_text(
    response_text,
    parse_mode='Markdown',
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("ارسال الملفات", url="https://t.me/sevanrussia")],
        [InlineKeyboardButton("الرجوع للقائمة", callback_data='parkenson')]
    ])
)
    elif query.data == 'medical_option_4':
     response_text = (
        "نبذة عن المشفى الذي يتم فيه إجراء العملية:\n\n"
        "Intelligent neurosurgery clinic»\n"
        "International medical center V.S. Buzaev memorial in Ufa city\n\n"
        "البروفيسور:\n"
        "*Neurosurgeon, MR-guided Focused Ultrasound Treatment of Movement Disorders*\n"
        "rezida maratovna galimova\n\n"
        "المشفى يعمل بهذه التقنية منذ عام 2020، وهو من أول المراكز في العالم التي تستخدم هذه التقنية لعلاج مرض باركنسون. "
        "وهو المركز الوحيد عالميًا الذي يعالج التصلب والبطء في الحركة، بينما باقي المراكز تعالج فقط الرعشة."
    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='parkenson')]]))
    elif query.data == 'medical_option_6':
     response_text = (
        "للسفر إلى روسيا لتلقي العلاج، هناك بعض الخطوات\n\n"
        " والإجراءات التي يجب اتباعها:\n"
        "1. *التأشيرة*:\n\n"
        " - لمواطني دول الخليج، يمكنهم التقديم للحصول على فيزا إلكترونية عبر الموقع الرسمي: [evisa.kdmid.ru](https://evisa.kdmid.ru). \n"
        "هذه الطريقة تسهل الحصول على التأشيرة بسرعة وبدون الحاجة للذهاب إلى السفارة.\n"
        "   - بالنسبة لمواطني الدول العربية الأخرى، يتعين عليهم الحصول على دعوة من المستشفى \n"
        " يجب الانتباه إلى أن هذه الدعوات قد تستغرق حوالي 45 يومًا لتجهز.\n\n "
        "2. *التخطيط للعلاج*: \n\n"
        "- من المهم التواصل معنا ل حجز موعد قبل حجز تذاكر الطيران  ."
        "3. *السفر*: \n\n"
        "  - بعد الحصول على التأشيرة، والتنسيق على موعد مع المشفى  يمكن حجز تذاكر الطيران وترتيب الإقامة في روسيا. \n\n"
        "المدينة التى يتم العلاج فيها هي مدينة أوفا الروسية Ufa Airport.\n"
    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='parkenson')]]))

    elif query.data == 'tour_1':
     response_text = (
    "تعتبر روسيا واحدة من أكبر وأغنى الدول في العالم من حيث التاريخ والثقافة والطبيعة. مع تنوعها الجغرافي والثقافي، تقدم روسيا تجربة سياحية فريدة ومثيرة للزوار من جميع أنحاء العالم. \n"
    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='tour')]]))

    elif query.data == 'tour_2':
     response_text = (
   "موسكو: \n\n"
   "الكرملين: يعد أحد أكبر القلاع في العالم وأحد أهم المعالم التاريخية في روسيا. \n"
   "الكاتدرائية المشرقة (كاتدرائية القديس باسيل): تتميز قبابها الملونة وتاريخها العريق \n"
   "ساحة الأحمر: وهي قلب موسكو التاريخي، وتعتبر مكانًا حيويًا للأنشطة الثقافية \n\n"
   "سانت بطرسبرغ: \n\n"
   "قصر الشتاء: مقر الإمبراطورة الروسية في السابق، ويضم الآن متحف هيرميتاج الشهير\n"
   "كنيسة المخلص على الدم: كنيسة رائعة تُعد مثالاً مميزاً للهندسة المعمارية الروسية.\n"
   "قناة نيفا: من أبرز معالم المدينة التي تقدم تجربة فريدة للزوار\n"
   "بحيرة بايكال:\n"
   "تُعتبر أعمق بحيرة في العالم وأحد أجمل المناطق الطبيعية في روسيا، حيث توفر فرصاً للرياضات المائية والمغامرات في الهواء الطلق\n"
   "الجبال الأورال: "
   "تعد وجهة شهيرة لمحبي الرياضات الشتوية والمشي لمسافات طويلة.\n\n"
   "مدينة كازان: \n"
   "وهي عاصمة جمهورية تتارستان، وتعد مزيجًا من الثقافة الروسية والميراث التتاري، مع معالم مثل الكرملين التتاري\n"

     )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='tour')]]))
    elif query.data == 'tour_3':
     response_text = (
        "موسكو:\n"
        "العاصمة الروسية وأكبر مدنها، تجمع بين التاريخ العريق والحداثة. هي المركز الثقافي والسياسي لروسيا، وتحتوي على معالم شهيرة ومراكز تسوق راقية.\n\n"
        "سانت بطرسبرغ:\n"
        "تعرف بمدينة البندقية الروسية، فهي مدينة تتميز بالقنوات والجسور الجميلة، فضلاً عن معالمها الثقافية مثل المتاحف والكنائس.\n\n"
        "سوتشي:\n"
        "منتجع ساحلي على البحر الأسود، مشهور بشواطئه ومرافقه الرياضية. استضافت الألعاب الأولمبية الشتوية 2014\n\n"
        "كازان:\n"
        "مدينة كبيرة تمتاز بمزيج من الثقافات الروسية والتتارية، وتعد مدينة ديناميكية مليئة بالمعالم الدينية والمعمارية\n" 
     )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='tour')]]))

    elif query.data == 'tour_4':
     response_text = (
"الإقامة:\n"
"الفنادق الاقتصادية: تتراوح الأسعار من 20 إلى 50 دولارًا أمريكيًا لليلة.\n"
"الفنادق المتوسطة: الأسعار تتراوح من 50 إلى 150 دولارًا أمريكيًا لليلة. \n"
"الفنادق الفاخرة: تبدأ من 150 دولارًا أمريكيًا وأكثر لليلة.\n\n"
"الطعام: \n"
"المطاعم الاقتصادية: تتراوح تكلفة الوجبة للشخص الواحد بين 5 إلى 10 دولار أمريكي.\n"
"المطاعم المتوسطة: تتراوح التكلفة بين 10 إلى 30 دولارًا أمريكيًا للوجبة.\n"
"المطاعم الراقية: قد تتجاوز تكلفة الوجبة للشخص الواحد 30 دولارًا أمريكيًا.\n\n"
"النقل:\n"
"التكاسي: يمكن أن تكون التكلفة في المدن الكبرى حوالي 1.5 إلى 3 دولارًا أمريكيًا للكيلومتر.\n"
"المواصلات العامة: وسائل النقل العامة مثل المترو والحافلات تكلف عادةً حوالي 0.5 إلى 1 دولار أمريكي.\n\n"
"الأنشطة السياحية:\n"
"الرحلات السياحية: الجولات في موسكو أو سانت بطرسبرغ قد تتراوح تكلفتها بين 20 إلى 50 دولارًا أمريكيًا للفرد.\n"
"الدخول إلى المتاحف والمعالم السياحية: مثل متحف هيرميتاج في سانت بطرسبرغ أو متحف الكرملين في موسكو، وتتراوح التذاكر من 5 إلى 20 دولارًا أمريكيًا حسب المعلم.\n"
    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='tour')]]))


    elif query.data == 'tour_5':
     response_text = (
"الربيع والصيف (من مايو إلى سبتمبر):\n"
"تعتبر هذه الفترة هي الأفضل للزيارة بسبب الطقس المعتدل والأجواء المريحة. في هذه الفترة، يمكن للزوار الاستمتاع بالأنشطة في الهواء الطلق، مثل زيارة الحدائق والمتاحف المفتوحة.\n\n"
"الخريف (أكتوبر إلى نوفمبر): \n"
"يمثل وقتًا جميلًا لزيارة روسيا للاستمتاع بتغيير الألوان في الطبيعة، خاصة في مدن مثل موسكو وسانت بطرسبرغ.\n\n"
"الشتاء (ديسمبر إلى فبراير): \n"
"تعتبر هذه الفترة مثالية لمحبي الرياضات الشتوية، مثل التزلج على الجليد في جبال الأورال أو في منتجع سوتشي."    )
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='tour')]]))
  
    elif query.data == 'tour_6':
     response_text = (
"تعد موسكو وسانت بطرسبرغ من أفضل المدن للتسوق، مع العديد من الأسواق والمولات الكبرى التي تقدم سلعًا روسية مميزة مثل الروسومات (المنتجات اليدوية التقليدية) والفرو والقطع الفنية.\n"
)
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='tour')]]))

    elif query.data == 'tour_7':
     response_text = (
"يحتاج معظم الزوار إلى تأشيرة سياحية لدخول روسيا. يمكن الحصول عليها من السفارات الروسية أو عبر الوكالات السياحية. \n"
" - لمواطني دول الخليج، يمكنهم التقديم للحصول على فيزا إلكترونية عبر الموقع الرسمي: [evisa.kdmid.ru](https://evisa.kdmid.ru). \n"
        "هذه الطريقة تسهل الحصول على التأشيرة بسرعة وبدون الحاجة للذهاب إلى السفارة.\n"
)
     await query.edit_message_text(response_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرجوع للقائمة", callback_data='tour')]]))



def main():
    application = Application.builder().token(TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
