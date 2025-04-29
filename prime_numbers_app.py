
import streamlit as st

st.set_page_config(page_title="آموزش اعداد اول", page_icon="📘")

st.markdown("<h1 style='text-align: right; color: green;'>آموزش اعداد اول با پایتون</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: right;'>تشکر بابت همکاری در این پژوهش، امیدوارم مفید واقع بشه.</p>", unsafe_allow_html=True)

st.write("### تعریف عدد اول:")
st.write("عدد اول، عددی بزرگتر از ۱ است که فقط دو مقسوم‌علیه دارد: ۱ و خودش.")

st.write("---")

number = st.number_input("یک عدد وارد کن:", min_value=2, step=1)

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if st.button("بررسی کن"):
    if is_prime(number):
        st.success(f"{number} یک عدد اول است.")
    else:
        st.error(f"{number} عدد اول نیست.")

st.write("---")

st.write("### نمایش اعداد اول تا عدد دلخواه:")

limit = st.slider("یک عدد انتخاب کن:", min_value=10, max_value=200, value=50)

primes = []
for num in range(2, limit+1):
    if is_prime(num):
        primes.append(num)

st.write(f"اعداد اول تا {limit}:")
st.code(primes)
