import 'package:flutter/material.dart';

class NeumorphicButton extends StatelessWidget {
  const NeumorphicButton({super.key, this.onPressed});

  final VoidCallback? onPressed;

  @override
  Widget build(BuildContext context) {
    return DecoratedBox(
      decoration: BoxDecoration(
        color: const Color(0xFFE6E7EE),
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: const Color(0xFF697386)),
        boxShadow: const [
          BoxShadow(color: Color(0xFFB8B9BE), offset: Offset(6, 6), blurRadius: 12),
          BoxShadow(color: Color(0xFFFFFFFF), offset: Offset(-6, -6), blurRadius: 12),
        ],
      ),
      child: TextButton(
        onPressed: onPressed,
        style: TextButton.styleFrom(
          minimumSize: const Size(44, 44),
          padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 12),
          foregroundColor: const Color(0xFF272B35),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
        ),
        child: const Text('Play'),
      ),
    );
  }
}
