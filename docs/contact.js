const form = document.getElementById('contact-form');
const submit = form.querySelector('button[type="submit"]');
const status = document.getElementById('contact-status');
let sending = false;
form.addEventListener('submit', async event => {
  event.preventDefault();
  if (sending || !form.reportValidity()) return;
  const value = id => document.getElementById(id).value.trim();
  const name = value('name'), email = value('email');
  const subject = value('subject'), message = value('message');
  status.hidden = false;
  if (!name || !subject || !message) {
    status.textContent = 'お名前・件名・お問い合わせ内容を入力してください。';
    return;
  }
  if (value('website')) {
    status.textContent = '入力内容を確認してください。';
    return;
  }
  const category = value('category');
  const data = {
    name, email, company: '', phone: '', agreed: document.getElementById('agree').checked,
    serviceId: 'fictionWarArchive', subject,
    message: `サイト：https://fiction-war-archive.birdman-studio.com/\nお問い合わせ種別：${category}\n\n${message}`,
    hp: ''
  };
  sending = true;
  submit.disabled = true;
  form.setAttribute('aria-busy', 'true');
  status.textContent = '送信しています…';
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 15000);
  try {
    const response = await fetch(form.dataset.endpoint, {
      method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({data}), signal: controller.signal, credentials: 'omit'
    });
    const payload = await response.json();
    if (!response.ok || payload.error || payload.result?.ok !== true) throw new Error('not-accepted');
    status.textContent = 'お問い合わせを受け付けました。返信・対応時期をお約束するものではありません。';
    form.reset();
  } catch {
    status.textContent = '受付結果を確認できませんでした。再送すると重複する場合があります。通信環境を確認するか、下記のメール窓口をご利用ください。入力内容は残しています。';
  } finally {
    clearTimeout(timer);
    sending = false;
    submit.disabled = false;
    form.removeAttribute('aria-busy');
  }
});
