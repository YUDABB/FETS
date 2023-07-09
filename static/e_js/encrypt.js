function encrypt() {
    const plaintext = document.getElementById("plaintext").value;
    const key = "mysecretkey"; // 암호화 키
    const encrypted = CryptoJS.AES.encrypt(plaintext, key).toString();
    document.getElementById("encrypted").value = encrypted;
}
