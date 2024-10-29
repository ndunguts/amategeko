document.getElementById('to-signup').addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector('.form-box').style.transform = 'rotateY(-180deg)';
});

document.getElementById('to-login').addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector('.form-box').style.transform = 'rotateY(0deg)';
});
