# Laravel

- Free and open-source PHP web framework
- **MVC** (model-view-controller) architecure

**Requirements**: PHP and Composer (installable via Homebrew on Mac)
`composer create-project laravel/laravel example-app; cd example-app; php artisan serve` --> localhost:8000

Available also on Docker.

*Config databases*

On local directory of the project -> `touch database/database.sqlite` (should already exists)
```sqlite
DB_CONNECTION=sqlite 
DB_CONNECTION=mysql 
DB_HOST=127.0.0.1 
DB_PORT=3306 
DB_DATABASE=laravel 
DB_USERNAME=root 
DB_PASSWORD= 
```
then, run: `php artisan migrate`

-----

## Lifecycle

1. In the project folder: public/index.html, the entrypoint.
All requests are directed to this file by the web server (Apaghe/Nginx) configuration.
Laravel, recieved a request create an instanche of the app/service container

2. Then `app/http/kernel.php` will detet the application enviroment and perform other task that need to be done before the request is actually handled.

3. **Service providers** is a very important phase, in this step, various components, such as database, queue, validation and routing components are bootstrapped.
All the service providers for the app are configured in the config/app.php in `providers` array (so iterating through this list and instantiate each of them)

4. **Routing** in the "App/Providers/RouteServiceProvider", this service loads the route files contained in the "routes" directory.
The router will dispatch the request to a route or controller, as well as run any route specific middleware.
However if the user is authenticated, the middleware will allow the request to preceed further in the application, like thiose definend in the $middleware property of HTTP kernel.

5. Once the route/controller method returns a response, the response will travel back outward through the route's middleware giving the app a change or examine the outgoing response

![Alt text](https://res.cloudinary.com/practicaldev/image/fetch/s--nEVwEz5T--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https%3A//dev-to-uploads.s3.amazonaws.com/i/7i2siqphm44ihjh4gfme.png)

## Service Container
A tool for managing class dependencies and prerforming dependency injection.
```php
<?php
namespace App\Http\Controllers;
use App\Http\Controllers\Controller;
use App\Repositories\UserRepository;
use App\Models\User;
class UserController extends Controller
{
    protected $users;
    // Create a new controller instance.
    public function __construct(UserRepository $users)
    {
        $this->users = $users;
    }
 
    // Show the profile for the given user.
    public function show($id)
    {
        $user = $this->users->find($id);
        return view('user.profile', ['user' => $user]);
    }
}
```
### Zero configuration resolution
```php
class Service{ }
Route::get("/",function(Service $service){
    die(get_class($service))
});
```
hitting the app "/" route will automatically resolve the "Service"

### Using the Container
```php
use Illuminate\Http\Request
Route::get("/",function(Request $request){
    //..
});
```
There is a dependencies injection behind the scenes, without interacting with the container we can easily access the current request.

### Binding
Almosst all of the service container bingings will be registered within service providers. With a service provider, we can always have access to the container via `$this->app` property.
We can register a binding using the bind method, passing the class or interface name we want to register, along with a closure that returns an instance of the class
```php
use App\Services\Transistor;
use App\Services\PodcastParser;

$this->app->bind(Transistor::class,function($app){
    return new Transistor($app-> make(PodcastParser::class));
})
```
Note that we receive the container itself as arugment to the resolver, we can use the container to resolve sub-dependencies of the object we're building.
Via App Facade we can interact with the container outisde of a service provider.
```php
use App\Services\Transistor;
use Illuminate\Support\Facades\App;

App::bind(Transistor::class,function($app){
    //
})
```
#### Singleton
The singleton method binds a class/interface into the contianer that should be resolved only one time.
Once singleton binding is resolved, the samoe object instance will be returned on subsequent calls into the container.

```php
use App\Services\Transistor;
use App\Services\PodcastParser;

$this->app->singleton(Transistor::class,function($app){
    return new Transistor($app->make(PodcastParser::class));
});

```
