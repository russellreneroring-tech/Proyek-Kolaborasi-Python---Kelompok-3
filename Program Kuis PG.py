# ==============================
# Program Kuis Pilihan Ganda
# ==============================

print("===== Selamat Datang di Kuis Python! =====")
print("Jawab pertanyaan dengan mengetik A, B, C, atau D\n")

score = 0


# Daftar pertanyaan (dictionary)
questions = [
    {
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