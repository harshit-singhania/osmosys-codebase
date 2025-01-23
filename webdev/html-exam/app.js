const toggleDarkMode = () => {
    const body = document.querySelector('body');
    body.classList.toggle('dark-mode');
};

const validateForm = () => {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if (name.trim() === '') {
        alert('Name is required');
        return false;
    }

    if (email.trim() === '') {
        alert('Email is required');
        return false;
    }

    if (!emailPattern.test(email)) {
        alert('Invalid email');
        return false;
    }

    return true;
}

const filterProjects = (category) => {
    const projects = document.querySelectorAll('.portfolio-item');
    projects.forEach(project => {
        if (category === 'all' || project.dataset.category === category) {
            project.style.display = 'block';
        } else {
            project.style.display = 'none';
        }
    });
};