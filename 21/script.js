// انتخاب عناصر HTML
const form = document.getElementById('statusForm');
const statusCodeInput = document.getElementById('statusCode');
const resultDiv = document.getElementById('result');

// افزودن رویداد برای ارسال فرم
form.addEventListener('submit', function (event) {
    event.preventDefault(); // جلوگیری از ارسال فرم پیش‌فرض

    const statusCode = statusCodeInput.value; // دریافت کد وارد شده توسط کاربر

    // بررسی خالی نبودن مقدار
    if (!statusCode) {
        resultDiv.innerHTML = `<p style="color:red;">Please enter a valid status code.</p>`;
        return;
    }

    // ایجاد URL تصویر
    const imageUrl = `https://http.cat/${statusCode}`;

    // تنظیم تصویر در DOM
    const img = document.createElement('img');
    img.src = imageUrl;
    img.alt = `HTTP Status ${statusCode}`;
    img.onload = () => resultDiv.innerHTML = ''; // پاک کردن متن قبلی پس از بارگذاری موفق تصویر
    img.onerror = () => resultDiv.innerHTML = `<p style="color:red;">No image found for status code ${statusCode}.</p>`;

    resultDiv.appendChild(img);
});
