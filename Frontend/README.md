# AI-Powered Outbound Sales Frontend

A professional React + TypeScript + Tailwind CSS frontend for the AI-based Outbound Sales platform featuring GenAI, Predictive Analytics, and CRM Integration for the IT Industry.

## 🚀 Features

### 📊 Dashboard
- Real-time statistics and KPIs
- Interactive charts (Area, Bar, Pie charts using Recharts)
- Lead score distribution visualization
- Revenue analytics
- Quick action cards for common workflows

### 👥 Lead Management
- Comprehensive lead table with search and filtering
- AI-powered lead scoring calculator
- Real-time lead score and conversion probability display
- Filter by score categories (High, Medium, Low)
- Visual score indicators with progress bars and badges

### ✉️ Email Campaign Generator
- AI-powered email generation using LLaMA 2
- Lead selection from high-value prospects
- Personalized content based on lead score and deal value
- SendGrid integration for automated email delivery
- Email preview and copy functionality
- Success notifications and delivery tracking

### 📈 Analytics Dashboard
- 6-month performance trends
- Conversion funnel visualization
- Lead quality metrics (Radar chart)
- Score distribution analysis
- Key insights and recommendations
- Performance KPIs with trend indicators

## 🛠️ Tech Stack

- **React 18** - Modern UI library
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Next-generation frontend tooling
- **Axios** - HTTP client for API calls
- **Recharts** - Composable charting library
- **Lucide React** - Beautiful icon library

## 📦 Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 🔧 Configuration

### Backend API Configuration

Update the API base URL in `src/services/api.ts`:

```typescript
const API_BASE_URL = 'http://localhost:8000';
```

###Tailwind Configuration

The Tailwind configuration is in `tailwind.config.js` with custom:
- Color palette (Primary, Secondary, Success, Warning, Danger)
- Animations (fade-in, slide-up, pulse-slow)
- Custom components (cards, buttons, inputs, badges)

## 🎨 Design System

### Colors
- **Primary**: Indigo gradient (for main actions)
- **Secondary**: Pink gradient (for secondary actions)
- **Success**: Green (for positive states)
- **Warning**: Yellow/Orange (for medium priority)
- **Danger**: Red (for alerts and low priority)

### Components
- **Cards**: Elevated white cards with shadow and hover effects
- **Buttons**: Gradient buttons with hover and active states
- **Inputs**: Focus ring and border animations
- **Badges**: Color-coded status indicators
- **Glass**: Glassmorphism effects for headers

### Animations
- Fade-in animations for page transitions
- Slide-up animations for modals
- Hover effects on interactive elements
- Pulse animations for loading states

## 📱 Pages & Features

### 1. Dashboard (`/`)
- Overview of all key metrics
- Visual analytics
- Quick navigation to other sections

### 2. Lead Management
- View and manage all leads
- Score new leads with AI
- Filter and search functionality
- Detailed lead information

### 3. Email Campaign
- Select high-value leads
- Generate AI-powered emails
- Send via SendGrid
- Track email delivery

### 4. Analytics
- In-depth performance metrics
- Trend analysis
- Conversion funnel
- Quality metrics

## 🔌 API Integration

The frontend connects to the FastAPI backend with the following endpoints:

- `GET /health` - Health check
- `GET /leads` - Fetch all leads
- `POST /predict` - Predict lead score
- `POST /generate-email-llama2` - Generate AI email
- `POST /send-email` - Send email via SendGrid

## 🎯 Key Components

### `Dashboard.tsx`
Main dashboard with statistics, charts, and quick actions.

### `LeadManagement.tsx`
Lead table, filtering, search, and AI scoring calculator.

### `EmailCampaign.tsx`
Email generation and sending interface with AI integration.

### `Analytics.tsx`
Advanced analytics with multiple chart types and insights.

### `Sidebar.tsx`
Navigation sidebar with active state management.

### `api.ts`
Centralized API service with TypeScript types.

## 🚀 Development

```bash
# Start development server with hot reload
npm run dev

# The app will be available at http://localhost:5173
```

## 🏗️ Build

```bash
# Create production build
npm run build

# The build output will be in the `dist` folder
```

## 📖 Usage

1. **Start the backend server** (FastAPI) on port 8000
2. **Start the frontend dev server**: `npm run dev`
3. **Open browser**: Navigate to `http://localhost:5173`
4. **Navigate** using the sidebar to access different features
5. **Score leads** using the AI calculator
6. **Generate emails** for high-value prospects
7. **Track performance** in the analytics dashboard

## 🎨 Customization

### Changing Colors
Edit `tailwind.config.js` to modify the color scheme:

```javascript
theme: {
  extend: {
    colors: {
      primary: { /* Your colors */ },
      secondary: { /* Your colors */ },
    }
  }
}
```

### Modifying Components
All reusable component styles are in `src/index.css` under the `@layer components` section.

## 🤝 Contributing

This is a production-ready application. For modifications:
1. Follow the existing component structure
2. Maintain TypeScript type safety
3. Use the established design system
4. Test all API integrations

## 📄 License

This project was built with professional standards for enterprise use.

## 🙏 Acknowledgments

- **LLaMA 2** for AI email generation
- **SendGrid** for email delivery
- **Recharts** for beautiful charts
- **Tailwind CSS** for styling
- **Lucide** for icons

---

**Built with ❤️ using React, TypeScript, and Tailwind CSS**
