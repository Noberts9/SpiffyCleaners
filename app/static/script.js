// Collapse navbar after clicking on a link (mobile only)
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    const navbarCollapse = document.querySelector('.navbar-collapse');
    if (navbarCollapse.classList.contains('show')) {
      new bootstrap.Collapse(navbarCollapse).toggle();
    }
  });
});

// Highlight active nav link on scroll
const sections = document.querySelectorAll("section, .container, footer");
const navLinks = document.querySelectorAll(".nav-link");

window.addEventListener("scroll", () => {
  let current = "";
  sections.forEach(section => {
    const sectionTop = section.offsetTop - 80;
    if (pageYOffset >= sectionTop) {
      current = section.getAttribute("id");
    }
  });

  navLinks.forEach(link => {
    link.classList.remove("active");
    if (link.getAttribute("href").includes(current)) {
      link.classList.add("active");
    }
  });
});
// Show/hide back to top button
const backToTop = document.getElementById("backToTop");

window.addEventListener("scroll", () => {
  if (window.scrollY > 300) {
    backToTop.style.display = "block";
  } else {
    backToTop.style.display = "none";
  }
});
const bookNowBtn = document.getElementById('bookNowBtn');
const bookingFormSection = document.getElementById('bookingFormSection');

bookNowBtn.addEventListener('click', () => {
  if (bookingFormSection.style.display === 'none' || bookingFormSection.style.display === '') {
    // Show form with drop-down effect
    bookingFormSection.style.display = 'block';
    bookingFormSection.style.animation = 'dropDown 0.4s ease forwards';
  } else {
    // Hide form
    bookingFormSection.style.animation = 'dropUp 0.4s ease forwards';
    setTimeout(() => {
      bookingFormSection.style.display = 'none';
    }, 400);
  }
});

const bookingForm = document.getElementById('bookingForm');

bookingForm.addEventListener('submit', function (event) {
  event.preventDefault();

  // Trigger built-in browser validation
  if (!bookingForm.checkValidity()) {
    bookingForm.classList.add('was-validated');
    return;
  }

  // If form is valid
  alert('Booking submitted!');
  bookingForm.reset();
  bookingForm.classList.remove('was-validated');
  bookingFormSection.style.animation = 'dropUp 0.4s ease forwards';
  setTimeout(() => {
    bookingFormSection.style.display = 'none';
  }, 400);
});
// Fade-in animation on scroll
const scrollElements = document.querySelectorAll('.animate-on-scroll');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, {
  threshold: 0.1,
});

scrollElements.forEach(el => observer.observe(el));

// Animate on scroll
function animateOnScroll() {
  const elements = document.querySelectorAll('.animate-on-scroll');
  const triggerBottom = window.innerHeight * 0.9;

  elements.forEach(el => {
    const top = el.getBoundingClientRect().top;
    if (top < triggerBottom) {
      el.classList.add('visible');
    }
  });
}

window.addEventListener('scroll', animateOnScroll);
window.addEventListener('load', animateOnScroll);

// Book button logic using Bootstrap Collapse
document.querySelectorAll('.book-btn').forEach(button => {
  button.addEventListener('click', () => {
    const selectedService = button.getAttribute('data-service');
    const formCollapse = document.getElementById('bookingFormContainer');

    if (formCollapse) {
      const bsCollapse = new bootstrap.Collapse(formCollapse, {
        toggle: false
      });
      bsCollapse.show();

      formCollapse.scrollIntoView({ behavior: 'smooth' });

      const serviceSelect = document.querySelector('#bookingForm select[name="service_type"]');
      if (serviceSelect) {
        serviceSelect.value = selectedService;
      }
    } else {
      alert('Booking form not found.');
    }
  });
});
