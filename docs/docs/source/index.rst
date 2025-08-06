.. title:: Xense

.. raw:: html

   <!DOCTYPE html>
   <html lang="zh-CN">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>千觉机器人 SDK 导航中心</title> 
      <script src="https://cdn.tailwindcss.com"></script>
      <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
      
      <!-- 配置Tailwind自定义主题 -->
      <script>
         tailwind.config = {
               theme: {
                  extend: {
                     colors: {
                           primary: '#3B82F6',
                           secondary: '#10B981',
                           accent: '#8B5CF6',
                           dark: '#1E293B',
                           light: '#F8FAFC'
                     },
                     fontFamily: {
                           sans: ['Inter', 'system-ui', 'sans-serif'],
                           display: ['Poppins', 'sans-serif']
                     },
                  }
               }
         }
      </script>
      
      <style type="text/tailwindcss">
         @layer utilities {
               .content-auto {
                  content-visibility: auto;
               }
               .text-shadow {
                  text-shadow: 0 2px 4px rgba(0,0,0,0.1);
               }
               .text-gradient {
                  background-clip: text;
                  -webkit-background-clip: text;
                  color: transparent;
               }
               .btn-hover {
                  @apply transition-all duration-300 transform hover:scale-105 hover:shadow-lg active:scale-95;
               }
               .bg-glass {
                  background: rgba(255, 255, 255, 0.1);
                  backdrop-filter: blur(10px);
                  -webkit-backdrop-filter: blur(10px);
               }
               .btn-container {
                  @apply flex flex-nowrap items-center justify-center gap-4 md:gap-6 w-full overflow-x-auto py-4;
               }
               .btn-custom {
                  @apply w-36 h-36 md:w-48 md:h-48;
               }
               /* 关键修改：针对Sphinx RTD主题的底部元素进行精准隐藏 */
               .rst-footer-buttons,  /* 隐藏Next/Previous按钮容器 */
               .wy-nav-content footer,  /* 隐藏默认页脚 */
               .relbar-bottom,  /* 隐藏底部导航条 */
               .rst-content .section:last-child  /* 隐藏可能的额外底部内容 */
               {
                  display: none !important;
                  visibility: hidden !important;
                  height: 0 !important;
                  margin: 0 !important;
                  padding: 0 !important;
               }
               /* 自定义页脚样式 */
               .custom-footer {
                  text-align: center;
                  padding: 20px 0;
                  color: #999;
                  margin-top: 40px;
               }
         }
      </style>
      
      <!-- 引入Google字体 -->
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
   </head>

   <body class="min-h-screen bg-gradient-to-br from-dark to-slate-800 text-light overflow-x-hidden">
      <!-- 背景动画元素 -->
      <div class="fixed inset-0 z-0 overflow-hidden">
         <div class="absolute -top-40 -left-40 w-80 h-80 bg-primary/20 rounded-full blur-3xl animate-pulse"></div>
         <div class="absolute top-1/3 -right-40 w-96 h-96 bg-accent/20 rounded-full blur-3xl animate-pulse" style="animation-delay: 1s"></div>
         <div class="absolute bottom-0 left-1/3 w-80 h-80 bg-secondary/20 rounded-full blur-3xl animate-pulse" style="animation-delay: 2s"></div>
      </div>

      <!-- 页面内容 -->
      <div class="relative z-10 container mx-auto px-4 py-16 md:py-24 flex flex-col items-center justify-center min-h-screen">
         <!-- 标题区域 -->
         <header class="text-center mb-16 md:mb-24">
               <h1 class="text-[clamp(2.5rem,6vw,4.5rem)] font-display font-bold leading-tight mb-4">
                  <span class="bg-gradient-to-r from-primary to-accent text-gradient">千觉机器人</span> 
               </h1>
               <p class="text-slate-300 text-lg md:text-xl max-w-2xl mx-auto">
                  探索我们的软件开发工具包，轻松集成强大功能到您的应用程序中
               </p>
         </header>

         <!-- 按钮容器 -->
         <div class="btn-container">
               <!-- XenseStudio 按钮 -->
               <a href="https://xense.readthedocs.io/en/latest/XenseStudio/Introduction.html" target="_blank" class="btn-hover btn-custom rounded-2xl bg-gradient-to-br from-purple-600 to-indigo-700 flex flex-col items-center justify-center p-4 shadow-2xl border border-purple-500/30 group">
                  <div class="w-12 h-12 mb-3 bg-white/20 rounded-full flex items-center justify-center backdrop-blur-sm transition-transform duration-300 group-hover:rotate-12">
                     <i class="fa fa-desktop text-white text-xl"></i>
                  </div>
                  <h2 class="text-xl md:text-2xl font-bold mb-1 text-white">XenseStudio</h2>
                  <p class="text-center text-white/80 text-xs">使用文档</p>
                  <span class="mt-2 inline-block bg-white/20 text-white text-xs px-2 py-0.5 rounded-full backdrop-blur-sm">
                     查看 <i class="fa fa-external-link ml-1 group-hover:translate-x-1 transition-transform"></i>
                  </span>
               </a>

               <!-- XenseSDK按钮 -->
               <a href="https://xense.readthedocs.io/en/latest/XenseSDK/XenseSDK.html" target="_blank" class="btn-hover btn-custom rounded-2xl bg-gradient-to-br from-primary to-blue-700 flex flex-col items-center justify-center p-4 shadow-2xl border border-primary/30 group">
                  <div class="w-12 h-12 mb-3 bg-white/20 rounded-full flex items-center justify-center backdrop-blur-sm transition-transform duration-300 group-hover:rotate-12">
                     <i class="fa fa-microchip text-white text-xl"></i>
                  </div>
                  <h2 class="text-xl md:text-2xl font-bold mb-1 text-white">XenseSDK</h2>
                  <p class="text-center text-white/80 text-xs">开发工具包</p>
                  <span class="mt-2 inline-block bg-white/20 text-white text-xs px-2 py-0.5 rounded-full backdrop-blur-sm">
                     查看 <i class="fa fa-external-link ml-1 group-hover:translate-x-1 transition-transform"></i>
                  </span>
               </a>


         <!-- 特性介绍 -->
         <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-20 w-full max-w-5xl">
               <div class="bg-glass rounded-xl p-6 border border-white/10 hover:border-primary/50 transition-colors duration-300">
                  <div class="w-12 h-12 bg-primary/20 rounded-lg flex items-center justify-center mb-4">
                     <i class="fa fa-code text-primary text-xl"></i>
                  </div>
                  <h3 class="text-xl font-semibold mb-2">简单集成</h3>
                  <p class="text-slate-300 text-sm">提供简洁API，轻松集成到现有项目中，减少开发时间</p>
               </div>
               
               <div class="bg-glass rounded-xl p-6 border border-white/10 hover:border-accent/50 transition-colors duration-300">
                  <div class="w-12 h-12 bg-accent/20 rounded-lg flex items-center justify-center mb-4">
                     <i class="fa fa-book text-accent text-xl"></i>
                  </div>
                  <h3 class="text-xl font-semibold mb-2">完善文档</h3>
                  <p class="text-slate-300 text-sm">详细的使用说明和示例代码，加速开发流程</p>
               </div>
               
               <div class="bg-glass rounded-xl p-6 border border-white/10 hover:border-secondary/50 transition-colors duration-300">
                  <div class="w-12 h-12 bg-secondary/20 rounded-lg flex items-center justify-center mb-4">
                     <i class="fa fa-life-ring text-secondary text-xl"></i>
                  </div>
                  <h3 class="text-xl font-semibold mb-2">技术支持</h3>
                  <p class="text-slate-300 text-sm">专业团队提供技术支持，解决集成过程中的问题</p>
               </div>
         </div>

         <!-- 自定义页脚 -->
         <div class="custom-footer">
               <p>© 2025 千觉机器人科技(上海)有限公司 | 版权所有</p>
         </div>
      </div>

      <!-- 交互脚本 -->
      <script>
         // 页面加载后执行隐藏操作，确保覆盖动态生成的元素
         document.addEventListener('DOMContentLoaded', () => {
               // 页面加载动画
               const elements = document.querySelectorAll('header, .btn-hover, .grid > div');
               elements.forEach((el, index) => {
                  el.style.opacity = '0';
                  el.style.transform = 'translateY(20px)';
                  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                  
                  setTimeout(() => {
                     el.style.opacity = '1';
                     el.style.transform = 'translateY(0)';
                  }, 100 + (index * 100));
               });

               // 强制隐藏底部不需要的元素，针对动态生成的内容
               const selectors = [
                  '.rst-footer-buttons',
                  '.wy-nav-content footer',
                  '.relbar-bottom',
                  '.rst-content .section:last-child',
                  '.next-button',
                  '.prev-button',
                  '.built-with-sphinx'
               ];
               
               selectors.forEach(selector => {
                  const elements = document.querySelectorAll(selector);
                  elements.forEach(el => {
                     el.style.display = 'none !important';
                     el.style.visibility = 'hidden !important';
                     el.style.height = '0 !important';
                  });
               });
         });
      </script>
   </body>
   </html>




|

.. toctree::
   :maxdepth: 1
   :caption: 主目录
   :hidden:

   XenseStudio/Introduction

   XenseSDK/XenseSDK




