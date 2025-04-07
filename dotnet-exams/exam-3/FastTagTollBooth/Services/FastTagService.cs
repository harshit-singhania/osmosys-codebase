using FastTagTollBooth.Data;
using FastTagTollBooth.Models;
using Microsoft.EntityFrameworkCore;

namespace FastTagTollBooth.Services {
    public class FastTagService : IFastTagService {
        private readonly FastTagDbContext _context;

        public FastTagService(FastTagDbContext context) {
            _context = context;
        }

        public async Task<FastTagVehicle?> GetByRegNumberAsync(string regNumber) {
            return await _context.FastTagVehicle
                .FirstOrDefaultAsync(v => v.RegNumber == regNumber);
        }

        public async Task<decimal?> GetBalanceAsync(string regNumber) {
            var vehicle = await GetByRegNumberAsync(regNumber);
            return vehicle?.Balance;
        }

        public async Task<decimal?> DeductBalanceAsync(string regNumber, decimal amount) {
            var vehicle = await GetByRegNumberAsync(regNumber);
            if (vehicle == null || vehicle.Balance < amount) {
                return null; // Not enough balance or vehicle not found
            }
            vehicle.Balance -= amount;
            await _context.SaveChangesAsync();
            return vehicle.Balance;
        }

    }
}