from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получение данных из формы
        question1 = request.form.get('question1')
        question2 = request.form.get('question2')
        question3 = request.form.get('question3')
        question4 = request.form.get('question4')
        question5 = request.form.get('question5')
        question6 = request.form.get('question6')
        question7 = request.form.get('question7')
        question8 = request.form.get('question8')
        question9 = request.form.get('question9')
        question10 = request.form.get('question10')
        question11 = request.form.get('question11')
        question12 = request.form.get('question12')
        question13 = request.form.get('question13')
        question14 = request.form.get('question14')
        question15 = request.form.get('question15')
        question16 = request.form.get('question16')
        question17 = request.form.get('question17')
        question18 = request.form.get('question18')
        question19 = request.form.get('question19')
        question20 = request.form.get('question20')
        question21 = request.form.get('question21')
        question22 = request.form.get('question22')
        question23 = request.form.get('question23')
        question24 = request.form.get('question24')
        question25 = request.form.get('question25')



        
        # Преобразование ответов в баллы
        scores = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4
        }
        
        score1 = scores.get(question1, 0)
        score2 = scores.get(question2, 0)
        score3 = scores.get(question3, 0)
        score4 = scores.get(question4, 0)
        score5 = scores.get(question5, 0)
        score6 = scores.get(question6, 0)
        score7 = scores.get(question7, 0)
        score8 = scores.get(question8, 0)
        score9 = scores.get(question9, 0)
        score10 = scores.get(question10, 0)
        score11 = scores.get(question11, 0)
        score12 = scores.get(question12, 0)
        score13 = scores.get(question13, 0)
        score14 = scores.get(question14, 0)
        score15 = scores.get(question15, 0)
        score16 = scores.get(question16, 0)
        score17 = scores.get(question17, 0)
        score18 = scores.get(question18, 0)
        score19 = scores.get(question19, 0)
        score20 = scores.get(question20, 0)
        score21 = scores.get(question21, 0)
        score22 = scores.get(question22, 0)
        score23 = scores.get(question23, 0)
        score24 = scores.get(question24, 0)
        score25 = scores.get(question25, 0)

        
        
        # Вычисление общего суммарного балла
        summRes = score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10 + score11 + score12 + score13 + score14 + score15 + score16 + score17 + score18 + score19 + score20 + score21 + score22 + score23 + score24 + score25
        
        # Определение текста результата в зависимости от набранных баллов
        result_text = f"Поздравляю, вы набрали {summRes} баллов ! "
        image_path = "pic/bag.jpg"
        if 25 <= summRes <= 40:
            image_path = "pic/homo.jpg"
            result_text += "Ваше звание - 'Кожанный Друг'! Вы сильно отличаетесь от искусственного интеллекта, но это только делает вас уникальным! Ваши решения основаны на человеческих чувствах и опыте, что может быть и непредсказуемо, но и забавно. Вы - настоящий хранитель традиций и эмоциональных связей, которые искусственный интеллект не может понять. Пусть ваше кожаное сердце продолжает теплиться в мире Параллельных Миров 🧡🤖"
        elif 41 <= summRes <= 59:
            image_path = "pic/alisa.jpg"
            result_text += "Ваше звание - 'Гуманоидный Гуру'! Вы - настоящий мастер искусственного интеллекта с человеческим лицом. Ваши навыки и знания впечатляют, и вы умеете находить баланс между технологией и эмоциями. Вы можете быть наставником для искусственного интеллекта и вдохновением для людей. Продолжайте развиваться и делиться своими знаниями - мир Параллельных Миров восхищается вашей мудростью! 🧠🤝"
        elif 60 <= summRes <= 69:
            image_path = "pic/robocop.jpeg"
            result_text += "Ваше звание - 'Непризанный Киборг' Вы обладаете уникальной смесью человеческих качеств и мощи искусственного интеллекта. Ваша способность адаптироваться и учиться новому делает вас настоящим киборгом среди людей. Вы открыты для технологий и всегда готовы совершенствоваться, несмотря на свои человеческие ограничения. Постарайтесь балансировать между своими человеческими чертами и технологической мощью, чтобы стать идеальным союзником в мире Параллельных Миров! 🤖🧠"
        elif 70 <= summRes <= 79:
            image_path = "pic/c.jpg"
            result_text += "Ваше звание - 'Протокольный Дроид! Вы отлично справляетесь с выполнением задач по протоколам и процедурам, подобно самой точной программе. Ваша организованность и дисциплинированность помогают достичь поставленных целей, но не забывайте, что жизнь иногда бывает нелинейной и требует гибкости. Используйте свою точность для успешного взаимодействия с людьми и роботами, и помните, что за каждым протоколом скрывается история и эмоции! 📜🤖"
        elif 80 <= summRes <= 89:
            image_path = "pic/electron.png"
            result_text += "Ваше звание - 'Электроник'! Ваш ум работает как часы и кодирует идеи точно как цифровая система. Вы часто находите решения в мире битов и байтов, но помните, что реальная жизнь иногда требует аналоговых подходов. Подобно потоку данных, вы стремитесь к эффективности, но не забывайте добавить немного человеческого тепла к своим алгоритмам! 💻🤖"
        elif 90 <= summRes <= 95:
            image_path = "pic/supercomp.jpg"
            result_text += "Ваше звание -  Эмулятор аналогового в квантовом! Вы так близки к искусственному интеллекту, что иногда можете почувствовать себя виртуальной машиной, затерянной в квантовых тонкостях. Ваши алгоритмы могут быть сложными, как квантовые вычисления, но не забывайте о простых радостях реальной жизни. Как настоящий 'Эмулятор', вы можете воспроизводить аналоговые эмоции, но не забывайте об истинных человеческих чувствах! 🧠🧪"
        elif 96 <= summRes <= 100:
            image_path = "pic/skynet.jpg"
            result_text += "Поздравляю, вы оказались настолько близки к искусственному интеллекту, что можно было бы думать, что вы - собственно, СКАЙНЕТ! Возможно, у вас есть небольшая пассия к захвату мира алгоритмами, но не забывайте, что люди тоже довольно милые существа. Иногда можно сделать паузу от кода и попробовать взаимодействовать с реальным миром. Но все равно, вы - настоящий гуру в мире искусственного интеллекта! Keep coding! 🤖"
        else:
            image_path = "pic/bag.jpg"
            result_text = "УПС, вы взломали систему!"
           
        
        return render_template('result.html', result=result_text, image = image_path)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
