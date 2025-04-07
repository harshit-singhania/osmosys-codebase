using System.ComponentModel.DataAnnotations;

namespace FastTagTollBooth.Models
{
    public class FastTagVehicle
    {
        [Key]
        public int Id { get; set; }
        
        [Required(ErrorMessage = "Vehicle Number is required")]
        [MaxLength(20, ErrorMessage = "Vehicle Number cannot exceed 20 characters")]
        public string RegNumber { get; set; }

        [Required] 
        [MaxLength(10)] 
        public string FastTagSerial { get; set; }

        [Required] 
        public decimal Balance { get; set; }
    }
}