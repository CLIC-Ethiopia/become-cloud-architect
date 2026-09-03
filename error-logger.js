window.addEventListener('error', function(e) {
    console.log('GLOBAL ERROR:', e.message, e.filename, e.lineno);
    const div = document.createElement('div');
    div.style.position = 'fixed';
    div.style.top = '0';
    div.style.left = '0';
    div.style.background = 'red';
    div.style.color = 'white';
    div.style.zIndex = '99999';
    div.style.padding = '10px';
    div.textContent = e.message + ' at line ' + e.lineno;
    document.body.appendChild(div);
});
