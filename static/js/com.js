$.ajax({
    type: "POST",
    url: "signup.html",
    data: $("#contactForm").serialize(),
    success: function () {
        alert("회원가입이 완료되었습니다.");
        window.location.href = "http://localhost:63342/%EB%A9%94%EC%9D%B8/startbootstrap-coming-soon-gh-pages/index.html";
    },
    error: function () {
        alert("회원가입에 실패했습니다.");
    }
});
