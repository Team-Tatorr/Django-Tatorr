# Django-Tatorr
<h1><b> This project is currenly inactive</b> </h1>
<h2>Project Structure</h2>

<p>By default the Django template loader will look within each app for a <code>templates</code> folder. But to avoid namespace issues you <em>also</em> need to repeat the app name in a folder below that before adding your template file.</p>
<p>For example, if we have <code>example_project</code> with a <code>pages</code> app and a <code>home.html</code> template file, the proper structure would be like this: within the <code>pages</code> app we create a <code>templates</code> directory, then a <code>pages</code> directory, and finally our <code>home.html</code> file.</p>
<div class="codehilite"><pre><span></span><span class="err">├── example_project</span>
<span class="err">│   ├── __init__.py</span>
<span class="err">│   ├── settings.py</span>
<span class="err">│   ├── urls.py</span>
<span class="err">│   └── wsgi.py</span>
<span class="err">|   └── pages</span>
<span class="err">|      ├── __init__.py</span>
<span class="err">│      ├── admin.py</span>
<span class="err">│      ├── apps.py</span>
<span class="err">│      ├── models.py</span>
<span class="err">│      ├── tests.py</span>
<span class="err">│      └── views.py</span>
<span class="err">|      ├── templates</span>
<span class="err">|          ├── pages</span>
<span class="err">|              ├── home.html</span>
<span class="err">└── manage.py</span>
</pre></div>
<p>This is demonstrated in the <a href="https://docs.djangoproject.com/en/dev/intro/">official Django polls tutorial</a> and works just fine.</p>
