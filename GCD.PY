import tkinter as tk
from tkinter import messagebox
import math

def calculate_gcd():
    try:
        # الحصول على القيم المدخلة من المستخدم
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        
        # التحقق من أن الأعداد موجبة
        if num1 <= 0 or num2 <= 0:
            messagebox.showerror("خطأ", "يرجى إدخال أعداد صحيحة موجبة فقط")
            return
        
        # حساب القاسم المشترك الأكبر
        result = math.gcd(num1, num2)
        
        # عرض النتيجة
        result_label.config(text=f"القاسم المشترك الأكبر هو: {result}")
        
    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال أعداد صحيحة فقط")
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ: {e}")

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("برمجة المهندس مازن درويش")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# إطار رئيسي
main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
main_frame.pack(expand=True, fill="both")

# عنوان التطبيق
title_label = tk.Label(main_frame, text="حاسبة القاسم المشترك الأكبر", 
                     font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# إطار المدخلات
input_frame = tk.Frame(main_frame, bg="#f0f0f0")
input_frame.pack(pady=10)

# ملصق وحقل إدخال الرقم الأول
label_num1 = tk.Label(input_frame, text="العدد الأول:", font=("Arial", 12), bg="#f0f0f0")
label_num1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_num1 = tk.Entry(input_frame, font=("Arial", 12), width=10)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

# ملصق وحقل إدخال الرقم الثاني
label_num2 = tk.Label(input_frame, text="العدد الثاني:", font=("Arial", 12), bg="#f0f0f0")
label_num2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_num2 = tk.Entry(input_frame, font=("Arial", 12), width=10)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# زر الحساب
calculate_button = tk.Button(main_frame, text="حساب", font=("Arial", 12, "bold"), 
                           bg="#4CAF50", fg="white", 
                           command=calculate_gcd, padx=20, pady=5)
calculate_button.pack(pady=15)

# ملصق النتيجة
result_label = tk.Label(main_frame, text="النتيجة ستظهر هنا", 
                      font=("Arial", 14), bg="#f0f0f0", fg="#333")
result_label.pack(pady=10)

# تضمين حقوق النشر
copyright_label = tk.Label(main_frame, text="© 2023 حاسبة القاسم المشترك الأكبر", 
                         font=("Arial", 8), bg="#f0f0f0", fg="#888")
copyright_label.pack(side="bottom", pady=5)

# تشغيل الحلقة الرئيسية للتطبيق
root.mainloop()
