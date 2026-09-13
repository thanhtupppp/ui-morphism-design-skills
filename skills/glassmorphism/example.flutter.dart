import 'dart:ui';
import 'package:flutter/material.dart';

class GlassSurface extends StatelessWidget {
  const GlassSurface({super.key, this.effectsEnabled = true, this.onPressed});

  final bool effectsEnabled;
  final VoidCallback? onPressed;

  @override
  Widget build(BuildContext context) {
    final surface = Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: effectsEnabled ? const Color(0x24FFFFFF) : Theme.of(context).colorScheme.surface,
        border: Border.all(color: effectsEnabled ? const Color(0x6BFFFFFF) : Theme.of(context).colorScheme.outline),
        borderRadius: BorderRadius.circular(20),
      ),
      child: FilledButton(
        onPressed: onPressed,
        style: FilledButton.styleFrom(minimumSize: const Size(44, 44)),
        child: const Text('Open panel'),
      ),
    );

    if (!effectsEnabled) return surface;

    return ClipRRect(
      borderRadius: BorderRadius.circular(20),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 20, sigmaY: 20),
        child: surface,
      ),
    );
  }
}
