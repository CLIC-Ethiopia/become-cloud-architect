const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
    const page = await browser.newPage();
    page.on('console', msg => console.log('PAGE LOG:', msg.text()));
    page.on('pageerror', error => console.log('PAGE ERROR:', error.message));
    
    await page.goto('http://localhost:3000');
    console.log('Page loaded');
    
    await page.click('#nav-iac');
    console.log('Clicked IaC');
    await new Promise(r => setTimeout(r, 1000));
    
    await browser.close();
})();
