## Routing
```php
use App\Http\Controllers\UserController;
 
Route::get('/user', [UserController::class, 'index']);
//Route::post($uri, $callback); || Route::put($uri, $callback); || Route::patch($uri, $callback); ...

//or
Route::match(['get', 'post'], '/', function () {
    //
});
 
Route::any('/', function () {
    //
});
```

### Redirect
```php
Route::redirect('/here', '/there'); //returns 302 status code
Route::permanentRedirect('/here', '/there'); //returns 301 status code
```


With `php artisan route:list -v` we can list all the routes that are defined in the app.
Or with `php artisan route:list --path=api` we can list all the routes that start with a given url (api)


### Parameters

```php
Route::get('/posts/{post}/comments/{comment}', function ($postId, $commentId) {
    //
});
//optional parameters
Route::get('/user/{name?}', function ($name = null) {
    return $name;
});
//Regex
Route::get('/user/{name}', function ($name) {
    //
})->where('name', '[A-Za-z]+');
//or simply wrapped into
Route::get('/category/{category}', function ($category) {
    //
})->whereIn('category', ['movie', 'song', 'painting']);
```

Determine if the current request was routed to a given named route.
```php
public function handle($request, Closure $next)
{
    if ($request->route()->named('profile')) {
        //
    }
 
    return $next($request);
}
```

### Controllers
```php
use App\Http\Controllers\OrderController;
 
Route::controller(OrderController::class)->group(function () {
    Route::get('/orders/{id}', 'show');
    Route::post('/orders', 'store');
});
```
Subdomain url
```php
use App\Http\Controllers\OrderController;
 
Route::controller(OrderController::class)->group(function () {
    Route::get('/orders/{id}', 'show');
    Route::post('/orders', 'store');
});
```
Route prefix
```php
Route::prefix('admin')->group(function () {
    Route::get('/users', function () {
        // Matches The "/admin/users" URL
    })->name("users");
});
```