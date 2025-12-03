# ==============================
# Program Kuis Pilihan Ganda
# ==============================

print("===== Selamat Datang di Kuis Python! =====")
print("Jawab pertanyaan dengan mengetik A, B, C, atau D\n")

score = 0


# Daftar pertanyaan (dictionary)
questions = [{
        "question": "1. Apa singkatan dari CPU?",
        "options": ["A. Central Processing Unit", 
                    "B. Control Primary Unit", 
                    "C. Central Print Unit", 
                    "D. Computer Power Unit"],
        "answer": "A"
     },
    {
        "question": "2. Tipe data apakah yang digunakan untuk bilangan desimal?",
        "options": ["A. int", 
                    "B. float", 
                    "C. string", 
                    "D. boolean"],
        "answer": "B"
    },
    {
        "question": "3. Bahasa pemrograman manakah yang paling mudah untuk pemula?",
        "options": ["A. Python", 
                    "B. Assembly", 
                    "C. C++", 
                    "D. Java"],
        "answer": "A"
    } 
]
for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    user_answer = input("Jawaban kamu: ").strip().upper()

    if user_answer == q["answer"]:
        print("Benar!\n")
        score += 1
    else:
        print(f"Salah! Jawaban yang benar adalah {q['answer']}\n")


print("===== HASIL AKHIR =====")
print(f"Skor kamu: {score} dari {len(questions)}")

if score == len(questions):
    print("Keren! Kamu menjawab semua dengan benar!")
elif score >= 2:
    print("Bagus! Kamu sudah cukup paham.")
else:
print("Jangan menyerah, terus belajar ya!")