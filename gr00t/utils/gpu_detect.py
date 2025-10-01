
def is_rtx_5000_series():
    """Check if the system has an RTX 5000-series GPU (e.g., RTX 5090)."""
    try:
        import torch
        if not torch.cuda.is_available():
            return False
        
        # Get the name of the first CUDA device
        gpu_name = torch.cuda.get_device_name(0)
        # RTX 5000-series cards typically include "50" in the model (e.g., "RTX 5090")
        return "RTX 50" in gpu_name
    
    except Exception:
        # If anything fails (no torch, no CUDA, etc.), assume not RTX 5000
        return False