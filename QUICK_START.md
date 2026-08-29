# Quick Start Guide - Skool Platform

## 🚀 Launch Your App in 30 Seconds

### **Option 1: Easiest Way (Recommended)**
1. Open folder: `C:\Users\ismai\OneDrive\Desktop\Skool\`
2. **Double-click** `run.bat` 
3. Your app opens automatically in your browser! ✨

### **Option 2: Manual - Double-Click HTML**
1. Open folder: `C:\Users\ismai\OneDrive\Desktop\Skool\`
2. **Double-click** `app.html`
3. App opens in your default browser

---

## What You Get

### 📚 Classroom Tab
- **All your courses** from export.json organized by section
- **Click any lesson** to see the full content
- **Video player** with chapters and timestamps
- **Download resources** (PDFs, docs, links)
- **Search** to find lessons quickly

### 💬 Community Tab
- **See all posts** from your community
- **Post new discussions** about anything
- **Upvote posts** you like (👍)
- **View comments** on posts
- **Your posts are saved** in your browser

### 🎨 Features
- **Dark/Light Theme** - Click 🌙/☀️ to switch
- **Mobile Friendly** - Works on phone, tablet, desktop
- **Super Fast** - Loads instantly
- **No Account Needed** - Just open and use!

---

## File Structure

```
C:\Users\ismai\OneDrive\Desktop\Skool\
│
├── app.html           ← Main application (open this!)
├── run.bat            ← Quick launcher script
├── README.md          ← Full documentation
├── QUICK_START.md     ← This file
│
├── export.json        ← Your data (lessons, posts, etc)
├── videos/            ← Your video files
│
├── index.html         ← Old version (ignore)
├── extract_links.py   ← Utility scripts
├── merge_media.py     │ (ignore for now)
└── get_missing_audio.py ┘
```

---

## Common Questions

### Q: Will my posts be saved?
**A:** Yes! Posts you create are saved in your browser. They persist until you clear browser data.

### Q: Can I share this with others?
**A:** Yes! Share the folder or just the `app.html` file. Others can open it in their browser.

### Q: Why use `run.bat` instead of just opening the HTML?
**A:** The batch file gives better compatibility with video streaming and modern web features.

### Q: Does it need internet?
**A:** Videos require internet (they stream from Mux/Vimeo). Everything else works offline.

### Q: Can I customize colors?
**A:** Yes! Edit `app.html` and find the CSS colors section at the top. All are clearly labeled.

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `F12` | Open developer console (for technical users) |
| `Tab` | Navigate between sections |
| `Ctrl+F` | Browser search (search bar at top is better) |

---

## Troubleshooting

### App doesn't open?
1. Try double-clicking `app.html` directly
2. Or run `run.bat` 
3. If still stuck, try another browser (Chrome, Edge, Firefox)

### Videos don't play?
1. Check your internet connection
2. Refresh the page (F5)
3. Try a different browser
4. Check that `export.json` has valid video data

### Posts not saving?
1. Make sure you're in the same browser
2. Don't use private/incognito mode
3. Check browser storage isn't disabled

### Looking blurry or tiny?
1. Adjust browser zoom: `Ctrl +` or `Ctrl -`
2. Or use the browser zoom button (⚙️)

---

## Next Steps

1. **[✓] Launch the app** - Run `run.bat` or open `app.html`
2. **[✓] Browse lessons** - Click courses in the sidebar
3. **[✓] Watch videos** - Click any lesson to play video
4. **[✓] Join community** - Switch to "Community" tab
5. **[✓] Create a post** - Share your thoughts!

---

## Want to Customize?

### Change Colors
Open `app.html` in any text editor (Notepad, VS Code, etc):
- Search for `:root {`
- Edit colors like `--primary: #2563eb;`
- Save and reload browser

### Change Title/Logo
- Search for "Skool" in the HTML
- Replace with your community name
- Save and reload

### Add More Features
- Extend the JavaScript section
- Add user profiles, messaging, etc.
- See `README.md` for advanced info

---

## Support Files

- **README.md** - Full documentation
- **app.html** - Complete source code (open in text editor to see it)
- **export.json** - Your data (JSON format)

---

## Tips for Best Experience

✅ Use **Chrome** or **Edge** for best performance  
✅ Keep **export.json** in the same folder  
✅ Use **run.bat** for video streaming support  
✅ Bookmark `http://localhost:8000/app.html` for quick access  
✅ Check **browser console** (F12) if something breaks  

---

**Ready? Launch the app now!** 🚀

```
Double-click: run.bat
OR
Double-click: app.html
```

Enjoy your community platform! 🎉
