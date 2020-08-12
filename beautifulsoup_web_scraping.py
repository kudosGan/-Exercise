<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf-8">

    <title>Jupyter Notebook</title>
    <link rel="shortcut icon" type="image/x-icon" href="/static/base/images/favicon.ico?v=97c6417ed01bdc0ae3ef32ae4894fd03">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="/static/components/jquery-ui/themes/smoothness/jquery-ui.min.css?v=9b2c8d3489227115310662a343fce11c" type="text/css" />
    <link rel="stylesheet" href="/static/components/jquery-typeahead/dist/jquery.typeahead.min.css?v=7afb461de36accb1aa133a1710f5bc56" type="text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    


<script type="text/javascript" src="/static/components/MathJax/MathJax.js?config=TeX-AMS-MML_HTMLorMML-full,Safe&delayStartupUntil=configured" charset="utf-8"></script>

<script type="text/javascript">
// MathJax disabled, set as null to distingish from *missing* MathJax,
// where it will be undefined, and should prompt a dialog later.
window.mathjax_url = "/static/components/MathJax/MathJax.js";
</script>

<link rel="stylesheet" href="/static/components/bootstrap-tour/build/css/bootstrap-tour.min.css?v=d0b3c2fce6056a2ddd5a4513762a94c4" type="text/css" />
<link rel="stylesheet" href="/static/components/codemirror/lib/codemirror.css?v=f25e9a9159e54b423b5a8dc4b1ab5c6e">


    <link rel="stylesheet" href="/static/style/style.min.css?v=29c09309dd70e7fe93378815e5f022ae" type="text/css"/>
    

<link rel="stylesheet" href="/static/notebook/css/override.css?v=e6f18013b8771987812e992b38ec3318" type="text/css" />
<link rel="stylesheet" href=""  id='kernel-css'                             type="text/css" />


    <link rel="stylesheet" href="/custom/custom.css" type="text/css" />
    <script src="/static/components/es6-promise/promise.min.js?v=f004a16cb856e0ff11781d01ec5ca8fe" type="text/javascript" charset="utf-8"></script>
    <script src="/static/components/preact/index.js?v=5b98fce8b86ce059de89f9e728e16957" type="text/javascript"></script>
    <script src="/static/components/proptypes/index.js?v=c40890eb04df9811fcc4d47e53a29604" type="text/javascript"></script>
    <script src="/static/components/preact-compat/index.js?v=d376eb109a00b9b2e8c0d30782eb6df7" type="text/javascript"></script>
    <script src="/static/components/requirejs/require.js?v=6da8be361b9ee26c5e721e76c6d4afce" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20200812043012",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jquery: 'components/jquery/jquery.min',
            bootstrap: 'components/bootstrap/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/ui/minified/jquery-ui.min',
            moment: 'components/moment/moment',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/dist/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })
    </script>

    
    

</head>

<body class="notebook_app "
 


  
    data-jupyter-api-token="65474f8726b4bd772f4f4e8219424dc928874bc1a4a15f41"
  
 
data-base-url="/"
data-ws-url=""
data-notebook-name="Untitled5-Copy2.ipynb"
data-notebook-path="Untitled5-Copy2.ipynb"

dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed.
  </div>
</noscript>

<div id="header">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand pull-left"><a href="/tree" title='dashboard'><img src='/static/base/images/logo.png?v=641991992878ee24c6f3826e81054a0f' alt='Jupyter Notebook'/></a></div>

  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  

  


<span id="save_widget" class="pull-left save_widget">
    <span id="notebook_name" class="filename"></span>
    <span class="checkpoint_status"></span>
    <span class="autosave_status"></span>
</span>

<span id="kernel_logo_widget">
  
  <img class="current_kernel_logo" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
  
</span>


  </div>
  <div class="header-bar"></div>

  
<div id="menubar-container" class="container">
<div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
            <button type="button" class="btn btn-default navbar-btn navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <i class="fa fa-bars"></i>
              <span class="navbar-text">Menu</span>
            </button>
            <p id="kernel_indicator" class="navbar-text indicator_area">
              <span class="kernel_indicator_name">Kernel</span>
              <i id="kernel_indicator_icon"></i>
            </p>
            <i id="readonly-indicator" class="navbar-text" title='This notebook is read-only'>
                <span class="fa-stack">
                    <i class="fa fa-save fa-stack-1x"></i>
                    <i class="fa fa-ban fa-stack-2x text-danger"></i>
                </span>
            </i>
            <i id="modal_indicator" class="navbar-text"></i>
            <span id="notification_area"></span>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">File</a>
                    <ul id="file_menu" class="dropdown-menu">
                        <li id="new_notebook" class="dropdown-submenu">
                            <a href="#">New Notebook</a>
                            <ul class="dropdown-menu" id="menu-new-notebook-submenu"></ul>
                        </li>
                        <li id="open_notebook"
                            title="Opens a new window with the Dashboard view">
                            <a href="#">Open...</a></li>
                        <!-- <hr/> -->
                        <li class="divider"></li>
                        <li id="copy_notebook"
                            title="Open a copy of this notebook's contents and start a new kernel">
                            <a href="#">Make a Copy...</a></li>
                        <li id="rename_notebook"><a href="#">Rename...</a></li>
                        <li id="save_checkpoint"><a href="#">Save and Checkpoint</a></li>
                        <!-- <hr/> -->
                        <li class="divider"></li>
                        <li id="restore_checkpoint" class="dropdown-submenu"><a href="#">Revert to Checkpoint</a>
                          <ul class="dropdown-menu">
                            <li><a href="#"></a></li>
                            <li><a href="#"></a></li>
                            <li><a href="#"></a></li>
                            <li><a href="#"></a></li>
                            <li><a href="#"></a></li>
                          </ul>
                        </li>
                        <li class="divider"></li>
                        <li id="print_preview"><a href="#">Print Preview</a></li>
                        <li class="dropdown-submenu"><a href="#">Download as</a>
                            <ul id="download_menu" class="dropdown-menu">
                                <li id="download_ipynb"><a href="#">Notebook (.ipynb)</a></li>
                                <li id="download_script"><a href="#">Script</a></li>
                                <li id="download_html"><a href="#">HTML (.html)</a></li>
                                <li id="download_markdown"><a href="#">Markdown (.md)</a></li>
                                <li id="download_rst"><a href="#">reST (.rst)</a></li>
                                <li id="download_latex"><a href="#">LaTeX (.tex)</a></li>
                                <li id="download_pdf"><a href="#">PDF via LaTeX (.pdf)</a></li>
                            </ul>
                        </li>
                        <li class="dropdown-submenu hidden"><a href="#">Deploy as</a>
                            <ul id="deploy_menu" class="dropdown-menu"></ul>
                        </li>
                        <li class="divider"></li>
                        <li id="trust_notebook"
                            title="Trust the output of this notebook">
                            <a href="#" >Trust Notebook</a></li>
                        <li class="divider"></li>
                        <li id="kill_and_exit"
                            title="Shutdown this notebook's kernel, and close this window">
                            <a href="#" >Close and Halt</a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Edit</a>
                    <ul id="edit_menu" class="dropdown-menu">
                        <li id="cut_cell"><a href="#">Cut Cells</a></li>
                        <li id="copy_cell"><a href="#">Copy Cells</a></li>
                        <li id="paste_cell_above" class="disabled"><a href="#">Paste Cells Above</a></li>
                        <li id="paste_cell_below" class="disabled"><a href="#">Paste Cells Below</a></li>
                        <li id="paste_cell_replace" class="disabled"><a href="#">Paste Cells &amp; Replace</a></li>
                        <li id="delete_cell"><a href="#">Delete Cells</a></li>
                        <li id="undelete_cell" class="disabled"><a href="#">Undo Delete Cells</a></li>
                        <li class="divider"></li>
                        <li id="split_cell"><a href="#">Split Cell</a></li>
                        <li id="merge_cell_above"><a href="#">Merge Cell Above</a></li>
                        <li id="merge_cell_below"><a href="#">Merge Cell Below</a></li>
                        <li class="divider"></li>
                        <li id="move_cell_up"><a href="#">Move Cell Up</a></li>
                        <li id="move_cell_down"><a href="#">Move Cell Down</a></li>
                        <li class="divider"></li>
                        <li id="edit_nb_metadata"><a href="#">Edit Notebook Metadata</a></li>
                        <li class="divider"></li>
                        <li id="find_and_replace"><a href="#"> Find and Replace </a></li>
                        <li class="divider"></li>
                        <li id="cut_cell_attachments"><a href="#">Cut Cell Attachments</a></li>
                        <li id="copy_cell_attachments"><a href="#">Copy Cell Attachments</a></li>
                        <li id="paste_cell_attachments" class="disabled"><a href="#">Paste Cell Attachments</a></li>
                        <li class="divider"></li>
                        <li id="insert_image" class="disabled"><a href="#"> Insert Image </a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">View</a>
                    <ul id="view_menu" class="dropdown-menu">
                        <li id="toggle_header"
                            title="Show/Hide the logo and notebook title (above menu bar)">
                            <a href="#">Toggle Header</a>
                        </li>
                        <li id="toggle_toolbar"
                            title="Show/Hide the action icons (below menu bar)">
                            <a href="#">Toggle Toolbar</a>
                        </li>
                        <li id="toggle_line_numbers"
                            title="Show/Hide line numbers in cells">
                            <a href="#">Toggle Line Numbers</a>
                        </li>
                        <li id="menu-cell-toolbar" class="dropdown-submenu">
                            <a href="#">Cell Toolbar</a>
                            <ul class="dropdown-menu" id="menu-cell-toolbar-submenu"></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Insert</a>
                    <ul id="insert_menu" class="dropdown-menu">
                        <li id="insert_cell_above"
                            title="Insert an empty Code cell above the currently active cell">
                            <a href="#">Insert Cell Above</a></li>
                        <li id="insert_cell_below"
                            title="Insert an empty Code cell below the currently active cell">
                            <a href="#">Insert Cell Below</a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Cell</a>
                    <ul id="cell_menu" class="dropdown-menu">
                        <li id="run_cell" title="Run this cell, and move cursor to the next one">
                            <a href="#">Run Cells</a></li>
                        <li id="run_cell_select_below" title="Run this cell, select below">
                            <a href="#">Run Cells and Select Below</a></li>
                        <li id="run_cell_insert_below" title="Run this cell, insert below">
                            <a href="#">Run Cells and Insert Below</a></li>
                        <li id="run_all_cells" title="Run all cells in the notebook">
                            <a href="#">Run All</a></li>
                        <li id="run_all_cells_above" title="Run all cells above (but not including) this cell">
                            <a href="#">Run All Above</a></li>
                        <li id="run_all_cells_below" title="Run this cell and all cells below it">
                            <a href="#">Run All Below</a></li>
                        <li class="divider"></li>
                        <li id="change_cell_type" class="dropdown-submenu"
                            title="All cells in the notebook have a cell type. By default, new cells are created as 'Code' cells">
                            <a href="#">Cell Type</a>
                            <ul class="dropdown-menu">
                              <li id="to_code"
                                  title="Contents will be sent to the kernel for execution, and output will display in the footer of cell">
                                  <a href="#">Code</a></li>
                              <li id="to_markdown"
                                  title="Contents will be rendered as HTML and serve as explanatory text">
                                  <a href="#">Markdown</a></li>
                              <li id="to_raw"
                                  title="Contents will pass through nbconvert unmodified">
                                  <a href="#">Raw NBConvert</a></li>
                            </ul>
                        </li>
                        <li class="divider"></li>
                        <li id="current_outputs" class="dropdown-submenu"><a href="#">Current Outputs</a>
                            <ul class="dropdown-menu">
                                <li id="toggle_current_output"
                                    title="Hide/Show the output of the current cell">
                                    <a href="#">Toggle</a>
                                </li>
                                <li id="toggle_current_output_scroll"
                                    title="Scroll the output of the current cell">
                                    <a href="#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_current_output"
                                    title="Clear the output of the current cell">
                                    <a href="#">Clear</a>
                                </li>
                            </ul>
                        </li>
                        <li id="all_outputs" class="dropdown-submenu"><a href="#">All Output</a>
                            <ul class="dropdown-menu">
                                <li id="toggle_all_output"
                                    title="Hide/Show the output of all cells">
                                    <a href="#">Toggle</a>
                                </li>
                                <li id="toggle_all_output_scroll"
                                    title="Scroll the output of all cells">
                                    <a href="#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_all_output"
                                    title="Clear the output of all cells">
                                    <a href="#">Clear</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Kernel</a>
                    <ul id="kernel_menu" class="dropdown-menu">
                        <li id="int_kernel"
                            title="Send KeyboardInterrupt (CTRL-C) to the Kernel">
                            <a href="#">Interrupt</a>
                        </li>
                        <li id="restart_kernel"
                            title="Restart the Kernel">
                            <a href="#">Restart</a>
                        </li>
                        <li id="restart_clear_output"
                            title="Restart the Kernel and clear all output">
                            <a href="#">Restart &amp; Clear Output</a>
                        </li>
                        <li id="restart_run_all"
                            title="Restart the Kernel and re-run the notebook">
                            <a href="#">Restart &amp; Run All</a>
                        </li>
                        <li id="reconnect_kernel"
                            title="Reconnect to the Kernel">
                            <a href="#">Reconnect</a>
                        </li>
                        <li id="shutdown_kernel"
                            title="Shutdown the Kernel">
                            <a href="#">Shutdown</a>
                        </li>
                        <li class="divider"></li>
                        <li id="menu-change-kernel" class="dropdown-submenu">
                            <a href="#">Change kernel</a>
                            <ul class="dropdown-menu" id="menu-change-kernel-submenu"></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Help</a>
                    <ul  id="help_menu" class="dropdown-menu">
                        
                        <li id="notebook_tour" title="A quick tour of the notebook user interface"><a href="#">User Interface Tour</a></li>
                        <li id="keyboard_shortcuts" title="Opens a dialog which shows all keyboard shortcuts"><a href="#">Keyboard Shortcuts</a></li>
                        <li id="edit_keyboard_shortcuts" title="Opens a dialog allowing you to edit Keyboard shortcuts"><a href="#">Edit Keyboard Shortcuts</a></li>
                        <li class="divider"></li>
                        

                        
                            
                                <li><a rel="noreferrer" href="http://nbviewer.ipython.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Notebook Help
                                </a></li>
                            
                                <li><a rel="noreferrer" href="https://help.github.com/articles/markdown-basics/" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Markdown
                                </a></li>
                            
                            
                        
                        <li class="divider"></li>
                        <li title="About Jupyter Notebook"><a id="notebook_about" href="#">About</a></li>
                        
                    </ul>
                </li>
              </ul>
            </div>
        </div>
    </div>
</div>

<div id="maintoolbar" class="navbar">
  <div class="toolbar-inner navbar-inner navbar-nobg">
    <div id="maintoolbar-container" class="container"></div>
  </div>
</div>
</div>

<div class="lower-header-bar"></div>

</div>

<div id="site">


<div id="ipython-main-app">
    <div id="notebook_panel">
        <div id="notebook"></div>
        <div id='tooltip' class='ipython_tooltip' style='display:none'></div>
    </div>
</div>



</div>



<div id="pager">
    <div id="pager-contents">
        <div id="pager-container" class="container"></div>
    </div>
    <div id='pager-button-area'></div>
</div>






<script type="text/javascript">
    sys_info = {"notebook_version": "5.0.0", "notebook_path": "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Anaconda3_64\\lib\\site-packages\\notebook", "commit_source": "", "commit_hash": "", "sys_version": "3.6.2 |Anaconda, Inc.| (default, Sep 19 2017, 08:03:39) [MSC v.1900 64 bit (AMD64)]", "sys_executable": "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Anaconda3_64\\python.exe", "sys_platform": "win32", "platform": "Windows-7-6.1.7601-SP1", "os_name": "nt", "default_encoding": "utf-8"};
</script>

<script src="/static/components/text-encoding/lib/encoding.js?v=d5bb0fc9ffeff7d98a69bb83daa51052" charset="utf-8"></script>

<script src="/static/notebook/js/main.min.js?v=6a166b31c5a20f809e44ec2d50e40412" type="text/javascript" charset="utf-8"></script>



<script type='text/javascript'>
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>
</body>

</html>