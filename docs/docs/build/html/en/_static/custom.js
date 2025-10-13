$(document).ready(function() {
    // 完全替换主题的导航处理逻辑
    if (typeof SphinxRtdTheme !== 'undefined' && typeof SphinxRtdTheme.Navigation !== 'undefined') {
        // 保存原始的 init 方法
        const originalInit = SphinxRtdTheme.Navigation.init;
        
        // 重写 init 方法
        SphinxRtdTheme.Navigation.init = function(n) {
            // 调用原始的初始化
            originalInit.call(this, n);
            
            // 修改菜单项的点击行为
            this.fixNavigationCollapse();
        };
        
        // 添加新方法来修复导航栏折叠问题
        SphinxRtdTheme.Navigation.fixNavigationCollapse = function() {
            const self = this;
            
            // 禁用所有菜单项的折叠行为
            $('.wy-menu-vertical a').off('click');
            
            // 为所有菜单项添加新的点击处理
            $('.wy-menu-vertical a').on('click', function(e) {
                // 高亮当前菜单项
                $('.wy-menu-vertical a').removeClass('current');
                $(this).addClass('current');
                
                // 确保所有父级菜单保持展开
                $(this).parents('li.toctree-l1, li.toctree-l2, li.toctree-l3').addClass('current').attr('aria-expanded', 'true');
                $(this).parents('ul').addClass('current').attr('aria-expanded', 'true');
                
                // 平滑滚动导航栏，确保当前菜单项可见
                const navBar = $('.wy-side-scroll');
                const itemTop = $(this).position().top;
                const itemHeight = $(this).outerHeight();
                const navHeight = navBar.height();
                const navScrollTop = navBar.scrollTop();
                
                if (itemTop < 0 || itemTop + itemHeight > navHeight) {
                    navBar.animate({
                        scrollTop: navScrollTop + itemTop - navHeight/2 + itemHeight/2
                    }, 300);
                }
            });
            
            // 初始化时展开所有菜单项
            $('.wy-menu-vertical li').addClass('current').attr('aria-expanded', 'true');
            $('.wy-menu-vertical ul').show();
        };
        
        // 初始化导航后立即修复折叠问题
        $(document).on('DOMContentLoaded', function() {
            if (SphinxRtdTheme.Navigation.isRunning) {
                SphinxRtdTheme.Navigation.fixNavigationCollapse();
            }
        });
    } else {
        // 如果主题API不可用，使用备用方法
        console.log('SphinxRtdTheme API not found, using fallback method');
        
        // 备用方法：直接修改菜单项行为
        $('.wy-menu-vertical a').on('click', function(e) {
            e.stopPropagation();
            $('.wy-menu-vertical a').removeClass('current');
            $(this).addClass('current');
            $(this).parents('li').addClass('current').attr('aria-expanded', 'true');
        });
        
        // 展开所有菜单项
        $('.wy-menu-vertical li').addClass('current').attr('aria-expanded', 'true');
        $('.wy-menu-vertical ul').show();
    }
});