// فعال‌سازی AOS
AOS.init({
    duration: 800,
    once: true,
    offset: 100
});

// مدیریت منوهای آبشاری
document.querySelectorAll('.dropdown-submenu').forEach(submenu => {
    const parentLink = submenu.querySelector('.dropdown-toggle');
    const childMenu = submenu.querySelector('.dropdown-menu');

    parentLink.addEventListener('click', (e) => {
        e.preventDefault();
        const isOpen = childMenu.classList.contains('show');
        document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
            menu.classList.remove('show');
        });
        if (!isOpen) {
            childMenu.classList.add('show');
        }
    });
});

document.addEventListener('click', (e) => {
    if (!e.target.closest('.dropdown-submenu')) {
        document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
            menu.classList.remove('show');
        });
    }
});

// جلوگیری از تغییر URL و نمایش زیرمنوها
document.querySelectorAll('.nav-item.dropdown > .nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const parent = link.parentElement;
        const isOpen = parent.classList.contains('show');
        document.querySelectorAll('.nav-item.dropdown').forEach(item => item.classList.remove('show'));
        if (!isOpen) {
            parent.classList.add('show');
        }
    });
});

document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav-item.dropdown')) {
        document.querySelectorAll('.nav-item.dropdown').forEach(item => item.classList.remove('show'));
    }
});

// مدیریت اسکرول هدر
let lastScroll = 0;
const header = document.querySelector('.ai-header');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > lastScroll && currentScroll > 100) {
        header.style.transform = 'translateY(-100%)';
    } else {
        header.style.transform = 'translateY(0)';
    }
    lastScroll = currentScroll;
});