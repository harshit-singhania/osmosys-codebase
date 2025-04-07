using FastTagTollBooth.Data;
using FastTagTollBooth.Services;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container
builder.Services.AddControllers();

// MySQL configuration
builder.Services.AddDbContext<FastTagDbContext>(options =>
    options.UseMySql(builder.Configuration.GetConnectionString("DefaultConnection"),
        new MySqlServerVersion(new Version(8, 0, 31))));

// Register FastTagService
builder.Services.AddScoped<IFastTagService, FastTagService>();

var app = builder.Build();

// Middleware pipeline (no Swagger or UI)
app.UseAuthorization();
app.MapControllers();

app.Run();
