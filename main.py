from ai import generate_ai_summary
from parsing import news_single

print("Quyidagilardan birini tanlang:")
print("1 - AI javobi")
print("2 - Yangiliklarni olish")
tanlov = input("Tanlovingizni kiriting (1 yoki 2): ")

if tanlov == "1":
    savol = input("AI ga savolingizni yozing: ")
    generate_ai_summary(savol)
elif tanlov == "2":
    news_single()
else:
    print("Noto'g'ri tanlov. Iltimos, 1 yoki 2 ni kiriting.")