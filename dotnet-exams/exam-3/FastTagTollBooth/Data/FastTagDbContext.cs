using Microsoft.EntityFrameworkCore;
using FastTagTollBooth.Models;

namespace FastTagTollBooth.Data {
    public class FastTagDbContext : DbContext
    {
        public FastTagDbContext(DbContextOptions<FastTagDbContext> options) : base(options)
        {
        }

        public DbSet<FastTagVehicle> FastTagVehicle { get; set; }
        
        protected override void OnModelCreating(ModelBuilder modelBuilder) {
            modelBuilder.Entity<FastTagVehicle>().HasIndex(v => v.RegNumber).IsUnique();
            modelBuilder.Entity<FastTagVehicle>()
                .HasIndex(v => v.FastTagSerial)
                .IsUnique();
        }
    }
}