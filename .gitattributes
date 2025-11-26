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
