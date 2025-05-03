document.querySelector('form').addEventListener('submit', (e) => {
  e.preventDefault();
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  if (!username || !password) {
    alert('لطفاً تمامی فیلدها را پر کنید.');
    return;
  }

  // ارسال اطلاعات به سرور (مثال)
  console.log('یوزرنیم:', username);
  console.log('رمز عبور:', password);
  alert('ورود با موفقیت انجام شد!');
});
