# 🚀 Skool Community Platform - Frontend

A modern, feature-rich web application for learning and community engagement built from your Skool data export.

## Features

### 📚 Classroom Features
- **Organized Course Structure** - Browse lessons organized by course, section, and topic
- **Video Player Integration** - Support for Mux and Vimeo hosted videos with direct playback
- **Video Chapters** - Auto-parsed chapter markers with timestamps
- **Lesson Resources** - Download resources (PDFs, docs) directly from lessons
- **Rich Descriptions** - Formatted lesson content with proper typography
- **Search** - Search across lessons, courses, and descriptions
- **Responsive Design** - Works on desktop, tablet, and mobile

### 💬 Community Features
- **Post Feed** - See all community posts and discussions
- **Create Posts** - Share thoughts, questions, and ideas
- **Upvote System** - Upvote posts you find valuable
- **Comments** - View and track comments on discussions
- **Discussion Integration** - See posts linked to specific lessons
- **Local Storage** - Your posts and upvotes persist locally

### 🎨 Design & UX
- **Dark/Light Theme Toggle** - Switch between themes instantly (persisted)
- **Modern UI** - Clean, professional design inspired by platforms like Skillshare and Udemy
- **Smooth Animations** - Subtle transitions and interactions
- **Accessibility** - Proper color contrast and keyboard navigation
- **Performance** - Lightweight and fast loading

## Getting Started

### Setup

1. **Place files in the same directory:**
   ```
   c:\Users\ismai\OneDrive\Desktop\Skool\
   ├── app.html          (main application)
   ├── export.json       (your data)
   ├── videos/           (video files folder)
   └── README.md         (this file)
   ```

2. **Open in browser:**
   - **Option A (Simple)**: Double-click `app.html` to open in your default browser
   - **Option B (Recommended)**: Use a local server for better compatibility
     ```bash
     # Using Python
     python -m http.server 8000
     
     # Using Node.js (if installed)
     npx http-server
     ```
   Then visit: `http://localhost:8000/app.html`

### Browser Support
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Usage

### Classroom Tab
1. **Browse Lessons** - Click on lessons in the left sidebar
2. **Watch Videos** - Videos play inline with chapter navigation
3. **View Resources** - Click resource cards to download/open
4. **Search** - Use the search bar to find specific content
5. **Track Progress** - Viewed lessons show a checkmark

### Community Tab
1. **Browse Posts** - Scroll through community discussions
2. **Create Post** - Type in the composer and click "Post"
3. **Upvote Posts** - Click the 👍 icon to show appreciation
4. **View Comments** - See discussions connected to each post

### Theme
- Click the 🌙/☀️ button in the top right to toggle dark/light mode
- Your preference is automatically saved

## Data Structure

The application reads from `export.json` which should contain:
- **Lessons** with course, section, and content information
- **Videos** hosted on Mux or Vimeo
- **Resources** (PDFs, links, files)
- **Community Posts** with author information and upvotes

## Customization

### Colors
Edit the CSS variables in the `<style>` section:
```css
:root {
  --primary: #2563eb;        /* Main blue accent */
  --secondary: #8b5cf6;      /* Purple accent */
  --success: #10b981;        /* Green for success */
  --danger: #ef4444;         /* Red for alerts */
  /* ... other colors */
}
```

### Styling
- Modify `.lesson-title`, `.post-card`, etc. for custom styling
- All colors automatically adapt to light/dark theme
- Responsive breakpoints at 768px and 640px

## Local Storage

The app saves to browser's local storage:
- `theme` - Your current theme preference
- `upvotedPosts` - Posts you've upvoted
- `communityPosts` - New posts you created locally

**Note:** Posts created locally are stored in your browser only. Refresh won't lose them, but changing browsers will.

## Troubleshooting

### Videos not playing?
- Ensure the playback tokens in export.json are valid
- Check your internet connection
- Try a different browser
- Some video providers (Vimeo) may require accepting cookies

### Data not loading?
- Verify `export.json` is in the same directory as `app.html`
- Check browser console (F12) for errors
- Ensure JSON file is valid

### Theme not persisting?
- Check if local storage is enabled in your browser
- Try clearing browser cache and reloading
- Check privacy/incognito settings

### Mobile not working?
- Ensure viewport meta tag is present (it is)
- Try landscape orientation
- Check browser zoom level

## Advanced Features

### Search
- Searches lesson titles, course names, and descriptions
- Results update in real-time as you type

### Auto-parsed Chapters
- Timestamps in descriptions are automatically detected
- Format: `HH:MM Video Title` or `HH:MM:SS Title`
- Click chapters to navigate to that timestamp

### Responsive Design
- Desktop (1024px+): Full sidebar + content
- Tablet (768px-1024px): Collapsible sidebar
- Mobile (<768px): Horizontal scroll sidebar, full-width content

## Browser DevTools

To access browser console for debugging:
1. Press `F12` or `Ctrl+Shift+I` (Windows) / `Cmd+Option+I` (Mac)
2. Go to "Console" tab
3. Type `console.log(allData)` to see loaded data

## Performance Tips

- **First Load**: Depends on export.json size (typically <1 second)
- **Video Streaming**: Depends on internet speed
- **Search**: Instant with <5000 lessons
- **Smooth Scrolling**: 60fps on modern devices

## Future Enhancements

Possible additions:
- User authentication
- Comments on posts
- Bookmark/favorite lessons
- Progress tracking
- Certificates of completion
- Discussion threads
- File uploads
- Direct messaging
- Admin dashboard

## Support

Issues or questions?
- Check browser console for error messages
- Verify all files are in the correct directory
- Clear browser cache and reload
- Try a different browser

## License

Created for your Skool community. Feel free to modify and customize!

---

**Version**: 1.0  
**Last Updated**: 2026-08-28  
**Built with**: HTML5, CSS3, JavaScript (Vanilla)
