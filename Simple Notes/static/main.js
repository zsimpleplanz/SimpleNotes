async function fetchNotes() {
  const res = await fetch('/api/notes');
  const notes = await res.json();
  renderNotes(notes);
}

function renderNotes(notes) {
  const list = document.getElementById('notes');
  list.innerHTML = '';
  for (const n of notes) {
    const li = document.createElement('li');
    li.className = 'note-item';

    const text = document.createElement('span');
    text.textContent = n.text;

    const meta = document.createElement('small');
    meta.className = 'muted';
    meta.textContent = new Date(n.created_at + 'Z').toLocaleString();

    const del = document.createElement('button');
    del.className = 'delete';
    del.textContent = '×';
    del.onclick = async () => {
      await fetch(`/api/notes/${n.id}`, { method: 'DELETE' });
      fetchNotes();
    };

    const rowTop = document.createElement('div');
    rowTop.className = 'row-top';
    rowTop.appendChild(text);
    rowTop.appendChild(del);

    const rowMeta = document.createElement('div');
    rowMeta.appendChild(meta);

    li.appendChild(rowTop);
    li.appendChild(rowMeta);
    list.appendChild(li);
  }
}

const form = document.getElementById('note-form');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const input = document.getElementById('note-input');
  const text = input.value.trim();
  if (!text) return;
  await fetch('/api/notes', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text })
  });
  input.value = '';
  fetchNotes();
});

fetchNotes();
