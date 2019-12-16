# -*- coding: utf-8 -*-
# rackio/api/config.py

## Base Modules

rackio_modules = [
    {'folder': 'static', 'subfolder': 'js', 'module': 'jquery.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'angular.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'angular-touch.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'angular-cookies.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'angular-animate.min.js'}, 
    {'folder': 'static', 'subfolder': 'js', 'module': 'angular-aria.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'angular-messages.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'angular-sanitize.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'angular-ui-router.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'd3.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'nv.d3.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'angular-nvd3.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'angular-material.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'angular-mocks.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'md-data-table.min.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'svg-assets-cache.js'},
    
]

## Admin Application Modules

admin_modules = [
    {'folder': 'static', 'subfolder': 'js', 'module': 'app.js'},
    {'folder': 'static', 'subfolder': 'js', 'module': 'index.js'},
]

admin_directives = [
    'messagesSection.js',
    'panelWidget.js',
]

admin_services = [
    'CountriesService.js',
    'MessagesService.js',
    'NavService.js',
    'PerformanceService.js',
    'TableService.js',
    'TodoListService.js',
]

admin_controllers = [
    'MainController.js',
    'ControlPanelController.js',
    'DataTableController.js',
    'MemoryController.js',
    'MessagesController.js',
    'PerformanceController.js',
    'ProfileController.js',
    'SearchController.js',
    'TableController.js',
    'TodoController.js',
    'UsageController.js',
    'VisitorsController.js',
    'WarningsController.js',
]

