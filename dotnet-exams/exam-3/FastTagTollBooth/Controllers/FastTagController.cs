using Microsoft.AspNetCore.Mvc;
using FastTagTollBooth.Services; 

namespace FastTagTollBooth.Controllers {
    [ApiController]
    [Route("api/[controller]")]
    public class FastTagController : ControllerBase {
        private readonly IFastTagService _service; 

        public FastTagController(IFastTagService service) {
            _service = service; 
        }

        // check the validity of the registration of the vehicle 
        [HttpGet("check-validity/{regNumber}")]
        public async Task<ActionResult> CheckValidity(string regNumber) {
            var vehicle = await _service.GetByRegNumberAsync(regNumber);
            return vehicle == null ? NotFound("Vehicle not found") : Ok("Vehicle is valid");
        }

        // check the balance of the vehicle
        [HttpGet("check-balance/{regNumber}")] 
        public async Task<IActionResult> CheckBalance(string regNumber) {
            var balance = await _service.GetBalanceAsync(regNumber);
            if (balance == null) {
                return NotFound("Vehicle not found or no balance available");
            }
            return Ok($"Balance: {balance}");
        }

        // deduct the balance of the vehicle if it is sufficient 
        // and return the new balance 
        [HttpPost("deduct/{regNumber}")]
        public async Task<IActionResult> DeductBalance(string regNumber, [FromQuery] decimal amount = 50) {
            try {
                var newBalance = await _service.DeductBalanceAsync(regNumber, amount); 
                return newBalance == null 
                    ? StatusCode(500, "Error: Vehicle not found or insufficient balance")
                    : Ok($"New balance: {newBalance}");
            } catch (Exception ex) {
                return StatusCode(500, $"Error: {ex.Message}");
            }
        }
    }
}