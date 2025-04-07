using FastTagTollBooth.Models;

namespace FastTagTollBooth.Services {
    public interface IFastTagService
    {
        Task<FastTagVehicle?> GetByRegNumberAsync(string regNumber); 
        Task<decimal?> GetBalanceAsync(string regNumber);
        Task<decimal?> DeductBalanceAsync(string regNumber, decimal amount);
    }
}